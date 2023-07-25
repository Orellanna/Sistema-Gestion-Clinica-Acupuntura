from datetime import date
from django.db import models
import base64

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.CharField(primary_key=True, max_length=10)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    fechanac_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=1)
    telefono_paciente = models.CharField(max_length=8, blank=True, null=True)
    email_paciente = models.CharField(max_length=50, blank=True, null=True)
    deshabilitado = models.BooleanField(default=False)
    fecharegistro_paciente = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id_paciente:  
            fecha_actual = date.today().strftime('%d%m%y')
            correlativo = self.obtener_correllativo(fecha_actual)
            self.id_paciente = self.generar_id_paciente(fecha_actual, correlativo)
            self.id_paciente = self.id_paciente.upper()
        super().save(*args, **kwargs)
        
    def obtener_correllativo(self,fecha_actual):
        pacientes_fecha_actual = Paciente.objects.filter(id_paciente__contains=fecha_actual)
        correlativo_actual = pacientes_fecha_actual.count() + 1
        
        correlativo_str = str(correlativo_actual).zfill(2)
        
        return correlativo_str
    
    def generar_id_paciente(self, fecha_actual, correlativo):
        
        primera_letra_nombre = self.primer_nombre[0]
        primera_letra_apellido = self.primer_apellido[0]
        
        id_paciente = f'{primera_letra_nombre}{primera_letra_apellido}{fecha_actual}{correlativo}'

        return id_paciente
        
    def __str__(self):
        return self.primer_nombre + ' ' + self.primer_apellido
    class Meta:
        managed = False
        db_table = 'paciente'
    
    def obtener_fechanac_formateada(self):
        return self.fechanac_paciente.strftime('%d / %B / %Y')
    
      
class Consulta(models.Model):
    id_consulta = models.CharField(primary_key=True, max_length=15)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    motivo_consulta = models.CharField(max_length=500)
    observacion_consulta = models.CharField(max_length=1000, blank=True, null=True)
    consulta_fecha = models.DateField()
    deshabilitado = models.BooleanField(default=False)
    hora_consulta = models.TimeField()

    def save(self, *args, **kwargs):
        if not self.id_consulta:  
            id_paciente = self.id_paciente.id_paciente
            id_paciente = id_paciente.upper()
            # Obtener el número de consultas previas para ese paciente
            consultas_previas = Consulta.objects.filter(id_paciente=self.id_paciente).count()
            numero_consulta = consultas_previas + 1
            # Crear el ID de la consulta en el formato requerido
            self.id_consulta = f'{id_paciente}C{numero_consulta:02}'
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.motivo_consulta + ' - ' + self.id_paciente.primer_nombre + ' ' + self.id_paciente.primer_apellido
    
    def obtener_consulta_fecha_formateada(self):
        return self.consulta_fecha.strftime('%d / %B / %Y')
    class Meta:
        managed = False
        db_table = 'consulta'
    
        
class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    cita_fecha = models.DateField()
    horainicio = models.TimeField()
    horafin = models.TimeField()
    observacion_cita = models.CharField(max_length=250, blank=True, null=True)
    estadocita = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cita'
        
class Terapia(models.Model):
    id_terapia = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta')
    observacion_terapia = models.CharField(max_length=150, blank=True, null=True)
    esquema_terapia = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'terapia'

class Inventario(models.Model):
    id_suministro = models.CharField(primary_key=True, max_length=10)
    nombre_suministro = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    costo_unitario = models.TextField()  # This field type is a guess.
    fecha_vencimiento = models.DateField()
    imagenprod = models.BinaryField(blank=True, null=True)
    
    def get_imagenprod_base64(self):
        if self.imagenprod:
            # Convertir los datos binarios a base64
            return base64.b64encode(self.imagenprod).decode('utf-8')
        return None

    def save(self, *args, **kwargs):
        if not self.id_suministro:  # Verificar si es un nuevo registro
            last_suministro = Inventario.objects.order_by('-id_suministro').first()
            last_id = last_suministro.id_suministro[1:] if last_suministro else "00000"
            new_id = f"{self.nombre_suministro[0].upper()}{str(int(last_id) + 1).zfill(5)}"
            self.id_suministro = new_id
        super(Inventario, self).save(*args, **kwargs)

    
    class Meta:
        managed = False
        db_table = 'inventario'

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    monto_pago = models.TextField()  # This field type is a guess.
    fecha_pago = models.DateField()
    concepto_pago = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'pago'
        



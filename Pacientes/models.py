from django.db import models

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


    def save(self, *args, **kwargs):
                if not self.id_paciente:  
                    nombre_paciente = self.id_paciente.primer_nombre
                    apellido_paciente = self.id_paciente.primer_apellido
                    id_paciente = (nombre_paciente[0] + apellido_paciente[0]).upper()
                            # Obtener el número de consultas previas para ese paciente
                    pacientes_previos = Paciente.objects.filter(id_paciente=self.id_paciente).count()
                    numero_paciente = pacientes_previos + 1
                            # Crear el ID del paciente en el formato requerido
                    self.id_paciente = f'{id_paciente}C{numero_paciente:02}'
                super().save(*args, **kwargs)
    def __str__(self):
        return self.primer_nombre + ' ' + self.primer_apellido
    class Meta:
        managed = False
        db_table = 'paciente'
<<<<<<< Updated upstream
        
=======
    
    def obtener_fechanac_formateada(self):
        return self.fechanac_paciente.strftime('%d-%m-%Y')
    
      
>>>>>>> Stashed changes
class Consulta(models.Model):
    id_consulta = models.CharField(primary_key=True, max_length=10)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    motivo_consulta = models.CharField(max_length=500)
    observacion_consulta = models.CharField(max_length=1000, blank=True, null=True)
    consulta_fecha = models.DateField()
    hora_consulta = models.TimeField()

    def save(self, *args, **kwargs):
        if not self.id_consulta:  
            nombre_paciente = self.id_paciente.primer_nombre
            apellido_paciente = self.id_paciente.primer_apellido
            id_paciente = (nombre_paciente[0] + apellido_paciente[0]).upper()
            # Obtener el número de consultas previas para ese paciente
            consultas_previas = Consulta.objects.filter(id_paciente=self.id_paciente).count()
            numero_consulta = consultas_previas + 1
            # Crear el ID de la consulta en el formato requerido
            self.id_consulta = f'{id_paciente}C{numero_consulta:02}'
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.motivo_consulta + ' - ' + self.id_paciente.primer_nombre + ' ' + self.id_paciente.primer_apellido
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
    id_suministro = models.AutoField(primary_key=True)
    nombre_suministro = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    costo_unitario = models.TextField()  # This field type is a guess.
    fecha_vencimiento = models.DateField()

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



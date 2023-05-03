from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self.primer_nombre + ' ' + self.primer_apellido
    
    class Meta:
        managed = False
        db_table = 'paciente'
        
class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    motivo = models.CharField(max_length=300)
    obervacion_consulta = models.CharField(max_length=500, blank=True, null=True)
    consulta_fecha = models.DateField()
    finalizada = models.BooleanField()

    def __str__(self):
        return self.motivo + ' - ' + self.id_paciente.primer_nombre + ' ' + self.id_paciente.primer_apellido
    
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


class Inspeccion(models.Model):
    id_inspeccion = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta')
    observacion_inspeccion = models.CharField(max_length=150, blank=True, null=True)
    esquema_inspeccion = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'inspeccion'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    monto = models.TextField()  
    fecha_pago = models.DateField()
    concepto_pago = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'pago'

class Inventario(models.Model):
    id_suministro = models.AutoField(primary_key=True)
    nombre_suministro = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    costo_unitario = models.TextField()  
    fecha_vencimiento = models.DateField()

    class Meta:
        managed = False
        db_table = 'inventario'
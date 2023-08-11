from django.contrib import admin
from .models import Paciente, Consulta, Pago, Terapia, Inventario, Citas


# Register your models here.
admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Pago)
admin.site.register(Terapia)
admin.site.register(Inventario)
admin.site.register(Citas)
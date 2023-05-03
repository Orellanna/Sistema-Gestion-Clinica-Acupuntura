from django.contrib import admin
from .models import Paciente, Consulta

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Consulta)

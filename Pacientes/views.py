from datetime import date, datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Paciente

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionPacientes(request):
    pacientes = Paciente.objects.all()

    # Iterar sobre cada paciente para calcular la edad
    for paciente in pacientes:
        fechanac_paciente = paciente.fechanac_paciente
        edad = CalcularEdad(fechanac_paciente)

    return render(request, 'Vistas_Pacientes/GestionPacientes.html', {
        'pacientes': pacientes,
        'edad':edad,
    })

@login_required
def DetallesConsulta(request):

    return render(request,'Vistas_Pacientes/DetallesConsulta.html')


@login_required
def DatosPersonales(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    fechanac_paciente = paciente.fechanac_paciente
    edad = CalcularEdad(fechanac_paciente)
    return render(request,'Vistas_Pacientes/DatosPersonales.html', {
        'paciente': paciente,
        'edad' : edad,
    })
    
def CalcularEdad(fechanac_paciente):
    hoy = date.today()
    edad = hoy.year - fechanac_paciente.year
    if hoy.month < fechanac_paciente.month or (hoy.month == fechanac_paciente.month and hoy.day < fechanac_paciente.day):
        edad -=1
    return edad

@login_required
def Registrar(request):
    return render(request,'Vistas_Pacientes/RegistrarPaciente.html')
    
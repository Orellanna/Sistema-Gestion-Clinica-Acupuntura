from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionPacientes(request):
    return render(request,'Vistas_Pacientes/GestionPacientes.html')

@login_required
def DetallesConsulta(request):
    return render(request,'Vistas_Pacientes/DetallesConsulta.html')

def DatosPersonales(request):
    return render(request,'Vistas_Pacientes/DatosPersonales.html')

@login_required
def Registrar(request):
    return render(request,'Vistas_Pacientes/RegistrarPaciente.html')
    
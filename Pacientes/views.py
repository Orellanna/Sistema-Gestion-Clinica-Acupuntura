from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def GestionPacientes(request):
    return render(request,'Vistas_Pacientes/GestionPacientes.html')

def DetallesConsulta(request):
    return render(request,'Vistas_Pacientes/DetallesConsulta.html')
#Borrar lo de abajo antes de subir cambio - Kevin
def Registrar(request):
    return render(request,'Vistas_Pacientes/RegistrarPaciente.html')
    
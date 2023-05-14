from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def GestionPacientes(request):
    return render(request,'GestionPacientes.html')

def DetallesConsulta(request):
    return render(request,'DetallesConsulta.html')

def NuevaConsulta(request):
    return render(request,'NuevaConsulta.html')   

def HistorialConsultas(request):
    return render(request,'HistorialConsultas.html')   
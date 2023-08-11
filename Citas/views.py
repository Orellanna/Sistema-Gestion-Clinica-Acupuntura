from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Pacientes.models import Citas
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from datetime import date, datetime

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionCitas(request):
    citas = Citas.objects.all()
        
    return render(request, 'Vistas_Citas/GestionCitas.html', {
        'citas': citas,
    })
@login_required
def RegistrarCitas(request):
    
    
    
       return render(request,'Vistas_Citas/RegistrarCitas.html')      
    

@login_required
def EliminarCitas(request):
    
    
    
       return render(request,'Vistas_Citas/EliminarCitas.html')      
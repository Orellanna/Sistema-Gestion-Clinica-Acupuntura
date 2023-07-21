from django.shortcuts import render
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from Pacientes.models import Inventario

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def ListarInventario(request):
    productos = Inventario.objects.all()
    
    return render(request,'Vistas_Inventario/GestionInventario.html',{
        'productos': productos,
    })



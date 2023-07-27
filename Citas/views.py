from django.shortcuts import render
from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Cita

@login_required
def index(request):
    return render(request,'index.html')


@login_required
def MostarCitas(request):
    citas = Cita.objects.all()
    
    return render(request,'Vistas_Citas/GestionCitas.html',{
        'citas': citas,
    })


   
    
    


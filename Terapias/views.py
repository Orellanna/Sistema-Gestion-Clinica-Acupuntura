from django.shortcuts import render
# Create your views here.
from Pacientes.models import Terapia
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def NuevaTerapia(request):
    return render(request,'Terapia/NuevaTerapia.html')
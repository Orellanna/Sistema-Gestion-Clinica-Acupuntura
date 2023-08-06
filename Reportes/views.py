from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Pacientes.models import Paciente
from Pacientes.models import Consulta
from Pacientes.views import CalcularEdad
from django.db.models import Q
from django.contrib import messages
from Pacientes.views import CalcularEdad
import base64
from django.db.models import Sum
import json

@login_required
def Reportes(request):
    return render(request, 'Reportes/reportes.html')

@login_required
def ListarReportes(request):
    numpacientes = Paciente.objects.all()
    numconsulta = Consulta.objects.all()
    total_pacientes = numpacientes.count()-7
    total_consulta = numconsulta.count()-4

    return render(request, 'Reportes/reportes.html', {
        'total_pacientes': total_pacientes,
        'total_consulta': total_consulta,
     
    })
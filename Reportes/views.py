from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Pacientes.models import Paciente
from Pacientes.models import Consulta
from django.db.models import Q
from django.contrib import messages
import base64
from django.db.models import Sum
import json

@login_required
def Reportes(request):
    return render(request, 'Reportes/reportes.html')

@login_required
def ListarReportes(request):
    numpacientes = Paciente.objects.filter(deshabilitado=False)
    numconsulta = Consulta.objects.filter(deshabilitado=False)
    total_pacientes = numpacientes.count()
    total_consulta = numconsulta.count()

    #calcular rangos de edades
    rangos_edad=[(0,18),(19,35),(36,50),(51,65),(66,100),]
    contador_edades=[]

    for rango_edad in rangos_edad:
        count= Paciente.objects.filter(
            deshabilitado=False,
            fechanac_paciente__lte=date.today()- timedelta(days=rango_edad[0]*365),
            fechanac_paciente__gt=date.today()- timedelta(days=rango_edad[1]*365),
        ).count()
        contador_edades.append(count)

    return render(request, 'Reportes/reportes.html', {
        'total_pacientes': total_pacientes,
        'total_consulta': total_consulta,
        'contador_edades': contador_edades,
    })
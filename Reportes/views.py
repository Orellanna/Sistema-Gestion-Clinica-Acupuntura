from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Pacientes.models import Paciente
from Pacientes.models import Consulta
from Pacientes.models import Pago
from Pacientes.models import Terapia
from django.db.models import Q
from django.contrib import messages
import base64
from django.db.models import Sum
import json
from django.db.models.functions import TruncMonth
from decimal import Decimal

@login_required
def Reportes(request):
    return render(request, 'Reportes/reportes.html')

@login_required
def ListarReportes(request):
    
    numpacientes = Paciente.objects.filter(deshabilitado=False)
    datospacientes = Paciente.objects.filter(deshabilitado=False)
    numconsulta = Consulta.objects.filter(deshabilitado=False)
    numTerapias = Terapia.objects.all()
    total_pacientes = numpacientes.count()
    total_consulta = numconsulta.count()
    total_terapias = numTerapias.count()

   # Obtener la lista de pacientes con su total de pagos
    listado_pacientes = []
    for paciente in datospacientes:
        total_pago = Pago.objects.filter(id_consulta__id_paciente=paciente.id_paciente).aggregate(total=Sum('monto_pago'))['total']
        paciente.total_pago = total_pago if total_pago else 0
        listado_pacientes.append(paciente)

   # Obtener ingresos por mes
    ingresos_por_mes = Pago.objects.annotate(month=TruncMonth('fecha_pago')).values('month').annotate(total_ingreso=Sum('monto_pago'))
    ingresos_mensuales = [0] * 12  # Inicializamos lista con ceros para cada mes

    for ingreso in ingresos_por_mes:
        mes = ingreso['month'].month - 1  # Los meses en Python comienzan desde 0
        monto_pago = ingreso['total_ingreso']
        if monto_pago and monto_pago[0] == '$':
            total_ingreso = monto_pago[1:].replace(',', '') # Eliminar símbolo "$" y comas
        else:
            total_ingreso = monto_pago if monto_pago else 0
        
        ingresos_mensuales[mes] = total_ingreso
    
    #calculo de los rangos de edades
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
        'pacientes': datospacientes,
        'total_pacientes': total_pacientes,
        'total_consulta': total_consulta,
        'contador_edades': contador_edades,
        'total_terapias': total_terapias,
        'ingresos_mensuales': ingresos_mensuales
    })


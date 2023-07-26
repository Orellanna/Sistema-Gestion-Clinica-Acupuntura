from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Pago, Consulta
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required
def NuevoPago(request):
    return render(request,'Vistas_Pago/NuevoPago.html')

@login_required
def ListarPagos(request, consulta_id):
    consulta = get_object_or_404(Consulta, id_consulta=consulta_id)
    pago = Pago.objects.filter(id_consulta=consulta_id)
    return render(request,'Vistas_Pago/HistorialPagos.html',{
        'pago': pago,
        'consulta': consulta,
    })

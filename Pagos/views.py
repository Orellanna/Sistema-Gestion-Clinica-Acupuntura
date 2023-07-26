from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Pago, Consulta, Paciente
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

def ListarPagos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pagos = Pago.objects.filter(id_consulta__id_paciente=paciente.id_paciente)
    
    return render(request, 'Vistas_Pago/HistorialPagos.html', {'paciente': paciente, 'pagos': pagos})

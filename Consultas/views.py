# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Pacientes.models import Consulta, Paciente


def index(request):
    return render(request,'index.html')

def DetallesConsulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, pk=consulta_id)
    paciente = consulta.id_paciente
    fecha_consulta_str = consulta.consulta_fecha.strftime('%d/%B/%Y')
    
    return render(request,'DetallesConsulta.html', {
        'consulta': consulta,
        'paciente': paciente,
        'fecha_consulta_str': fecha_consulta_str,
    })
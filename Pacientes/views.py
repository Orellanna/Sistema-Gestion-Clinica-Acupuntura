from datetime import date, datetime
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Paciente
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionPacientes(request):
    return render(request,'Vistas_Pacientes/GestionPacientes.html')

@login_required
def DetallesConsulta(request):

    return render(request,'Vistas_Pacientes/DetallesConsulta.html')


@login_required
def DatosPersonales(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    fechanac_paciente = paciente.fechanac_paciente
    edad = CalcularEdad(fechanac_paciente)
    return render(request,'Vistas_Pacientes/DatosPersonales.html', {
        'paciente': paciente,
        'edad' : edad,
    })
    
def CalcularEdad(fechanac_paciente):
    hoy = date.today()
    edad = hoy.year - fechanac_paciente.year
    if hoy.month < fechanac_paciente.month or (hoy.month == fechanac_paciente.month and hoy.day < fechanac_paciente.day):
        edad -=1
    return edad

@login_required
def Registrar(request):
    return render(request,'Vistas_Pacientes/RegistrarPaciente.html')

@login_required
def EditarPaciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente = paciente_id)
    #lo q esta en corchetes es el nombre del campo en la vista
    #o es el nombre del campo en el model
    if request.method == 'POST':
        primer_nombre = request.POST['primer_nombre']
        segundo_nombre = request.POST['segundo_nombre']
        primer_apellido = request.POST['primer_apellido']
        segundo_apellido = request.POST['segundo_apellido']
        fechanac_paciente = request.POST['fechanac_paciente']
        sexo_paciente = request.POST['sexo_paciente']
        telefono_paciente = request.POST['telefono_paciente']
        email_paciente = request.POST['email_paciente']
        
        paciente.primer_nombre = primer_nombre
        paciente.segundo_nombre = segundo_nombre
        paciente.primer_apellido = primer_apellido
        paciente.segundo_apellido = segundo_apellido
        paciente.fechanac_paciente = fechanac_paciente
        paciente.sexo_paciente = sexo_paciente
        paciente.telefono_paciente = telefono_paciente
        paciente.email_paciente = email_paciente
        paciente.save()
        #esto no lo entiendo
        url = reverse('DatosPersonales', kwargs={'paciente_id': paciente_id})
        
        return redirect(url)
    return render(request,'Vistas_Pacientes/EditarPaciente.html', {'paciente': paciente})


    
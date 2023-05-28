from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Paciente
from django.db.models import Q

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionPacientes(request):
    pacientes = Paciente.objects.all()
    fecha_actual = datetime.today()

    for paciente in pacientes:
        edad= fecha_actual.year - paciente.fechanac_paciente.year
        if fecha_actual.month < paciente.fechanac_paciente.month and fecha_actual.day < paciente.fechanac_paciente.day:
            edad -=1
        elif fecha_actual.month == paciente.fechanac_paciente.month and fecha_actual.day < paciente.fechanac_paciente.day:
            edad -=1
        paciente.edad = edad    
            

    return render(request, 'Vistas_Pacientes/GestionPacientes.html', {
        'pacientes': pacientes,
    })

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
    
    if request.method == 'POST':
        primer_nombre = request.POST['primer_nombre']
        primer_apellido = request.POST['primer_apellido']
        fechanac_paciente = request.POST['fechanac_paciente']
        sexo_paciente = request.POST['sexo_paciente']
        telefono_paciente = request.POST['telefono_paciente']
        email_paciente = request.POST['email_paciente']
        
        nuevo_paciente = Paciente()
        nuevo_paciente.primer_nombre = primer_nombre
        nuevo_paciente.primer_apellido = primer_apellido
        nuevo_paciente.fechanac_paciente = fechanac_paciente
        nuevo_paciente.sexo_paciente = sexo_paciente
        nuevo_paciente.telefono_paciente = telefono_paciente
        nuevo_paciente.email_paciente = email_paciente
        nuevo_paciente.save()
        
        return redirect('GestionPacientes')
         
    return render(request,'Vistas_Pacientes/registrarPaciente.html')
    

@login_required
def EditarPaciente(request, id_paciente):
    
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    
    if request.method == 'POST':
        primer_nombre = request.POST['primer_nombre']
        primer_apellido = request.POST['primer_apellido']
        fechanac_paciente = request.POST['fechanac_paciente']
        sexo_paciente = request.POST['sexo_paciente']
        telefono_paciente = request.POST['telefono_paciente']
        email_paciente = request.POST['email_paciente']
        
        paciente.primer_nombre = primer_nombre
        paciente.primer_apellido = primer_apellido
        paciente.fechanac_paciente = fechanac_paciente
        paciente.sexo_paciente = sexo_paciente
        paciente.telefono_paciente = telefono_paciente
        paciente.email_paciente = email_paciente
    
        paciente.save()
        
        return redirect('GestionPacientes')
    
    return render(request,'Vistas_Pacientes/EditarPaciente.html', {
        'paciente': paciente,
    })
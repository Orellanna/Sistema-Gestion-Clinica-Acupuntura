from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from Pacientes.models import Consulta, Paciente
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionPacientes(request):
    return render(request,'Vistas_Pacientes/GestionPacientes.html')

@login_required
def DetallesConsulta(request):
    return render(request,'Vistas_Pacientes/DetallesConsulta.html')

def DatosPersonales(request):
    return render(request,'Vistas_Pacientes/DatosPersonales.html')

@login_required
def Registrar(request, id_paciente, primer_nombre, segundo_nombre, primer_apellido , segundo_apellido, edad_paciente, sexo_paciente, telefono_paciente, email_paciente)

    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    
    if request.method == 'POST':

        primer_nombre     = request.POST['InputPrimerNombre']
        segundo_nombre    = request.POST['InputSegundoNombre']
        primer_apellido   = request.POST['InputPrimerApellido']
        segundo_apellido  = request.POST['InputSegundoApellido']
        edad_paciente     = request.POST['InputEdad'] 
        sexo_paciente     = request.POST['SelectSexo']
        telefono_paciente = request.POST['InputTelefono']
        email_paciente    = request.POST['InputCorreo']
 
        # Creamos la nueva consulta para el paciente
        paciente = Paciente.objects.create(
            
            
            
            id_paciente       = id_paciente,
            primer_nombre     = primer_nombre
            segundo_nombre    = segundo_nombre
            primer_apellido   = primer_apellido
            segundo_apellido  = segundo_apellido
            edad_paciente     = edad_paciente 
            sexo_paciente     = sexo_paciente
            telefono_paciente = telefono_paciente
            email_paciente    = email_paciente
        )
            
     
    return render(request,'Vistas_Pacientes/RegistrarPaciente.html')
    
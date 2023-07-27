from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from Pacientes.models import Consulta, Paciente
from django.views.decorators.csrf import csrf_exempt, GestionPacientes
from django.urls import reverse


@login_required
def index(request):
    return render(request,'index.html')

@login_required
def GestionPacientes(request):

    pacientes = Paciente.objects.all().values()

    return render(request,'Vistas_Pacientes/GestionPacientes.html')

@login_required
def DetallesConsulta(request):
    return render(request,'Vistas_Pacientes/DetallesConsulta.html')

@login_required
def EditarPaciente(request, id_paciente, primer_nombre, segundo_nombre, primer_apellido , segundo_apellido, edad_paciente, sexo_paciente, telefono_paciente, email_paciente):

    
    Paciente = get_object_or_404(Paciente, primer_nombre=primer_nombre)
    Paciente = get_object_or_404(Paciente, segundo_nombre=segundo_nombre)
    Paciente = get_object_or_404(Paciente, primer_apellido=primer_apellido)
    Paciente = get_object_or_404(Paciente, segundo_apellido=segundo_apellido)
    Paciente = get_object_or_404(Paciente, edad_paciente=edad_paciente)
    Paciente = get_object_or_404(Paciente, sexo_paciente=sexo_paciente)
    Paciente = get_object_or_404(Paciente, telefono_paciente=telefono_paciente)
    Paciente = get_object_or_404(Paciente, email_paciente=email_paciente)

    
    if request.method == 'POST':

        primer_nombre     = request.POST['InputPrimerNombre']
        segundo_nombre    = request.POST['InputSegundoNombre']
        primer_apellido   = request.POST['InputPrimerApellido']
        segundo_apellido  = request.POST['InputSegundoApellido']
        edad_paciente     = request.POST['InputEdad'] 
        sexo_paciente     = request.POST['SelectSexo']
        telefono_paciente = request.POST['InputTelefono']
        email_paciente    = request.POST['InputCorreo']
 
        # modificacion de los campos del paciente
        Paciente = Paciente.objects.get(
            
            primer_nombre     = primer_nombre,
            segundo_nombre    = segundo_nombre,
            primer_apellido   = primer_apellido,
            segundo_apellido  = segundo_apellido,
            edad_paciente     = edad_paciente,
            sexo_paciente     = sexo_paciente,
            telefono_paciente = telefono_paciente,
            email_paciente    = email_paciente,
        )
        # Generamos la URL correcta usando reverse
        url = reverse('GestionPacientes', kwargs={'paciente_id': id_paciente})
        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)




    return render(request,'Vistas_Pacientes/EditarPaciente.html')


def DatosPersonales(request):



    return render(request,'Vistas_Pacientes/DatosPersonales.html')

@login_required
def Registrar(request, id_paciente, primer_nombre, segundo_nombre, primer_apellido , segundo_apellido, edad_paciente, sexo_paciente, telefono_paciente, email_paciente):

    Paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    Paciente = get_object_or_404(Paciente, primer_nombre=primer_nombre)
    Paciente = get_object_or_404(Paciente, segundo_nombre=segundo_nombre)
    Paciente = get_object_or_404(Paciente, primer_apellido=primer_apellido)
    Paciente = get_object_or_404(Paciente, segundo_apellido=segundo_apellido)
    Paciente = get_object_or_404(Paciente, edad_paciente=edad_paciente)
    Paciente = get_object_or_404(Paciente, sexo_paciente=sexo_paciente)
    Paciente = get_object_or_404(Paciente, telefono_paciente=telefono_paciente)
    Paciente = get_object_or_404(Paciente, email_paciente=email_paciente)

    
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
        Paciente = Paciente.objects.create(
            id_paciente       = id_paciente,
            primer_nombre     = primer_nombre,
            segundo_nombre    = segundo_nombre,
            primer_apellido   = primer_apellido,
            segundo_apellido  = segundo_apellido,
            edad_paciente     = edad_paciente,
            sexo_paciente     = sexo_paciente,
            telefono_paciente = telefono_paciente,
            email_paciente    = email_paciente,
        )
        # Generamos la URL correcta usando reverse
        url = reverse('GestionPacientes', kwargs={'paciente_id': id_paciente})
        
<<<<<<< Updated upstream
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
            
     
    return render(request,'Vistas_Pacientes/RegistrarPaciente.html')
    
=======
        paciente.primer_nombre = primer_nombre
        paciente.segundo_nombre = segundo_nombre
        paciente.primer_apellido = primer_apellido
        paciente.segundo_apellido = segundo_apellido
        paciente.fechanac_paciente = fechanac_paciente
        paciente.sexo_paciente = sexo_paciente
        paciente.telefono_paciente = telefono_paciente
        paciente.email_paciente = email_paciente
    
        paciente.save()
        messages.warning(request, "El Paciente se ha editado satisfactoriamente")
        return redirect('DatosPersonales', id_paciente=id_paciente)
    
    return render(request,'Vistas_Pacientes/EditarPaciente.html', {
        'paciente': paciente,
    })
    

@login_required
def EliminarPaciente(request, id_paciente):
    
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    
    # Deshabilitar al paciente
    paciente.deshabilitado = True
    paciente.save()

    # Redirigir a la página de gestión de pacientes
    messages.success(request, "El Paciente se ha desactivado satisfactoriamente")
    return redirect('GestionPacientes')
>>>>>>> Stashed changes

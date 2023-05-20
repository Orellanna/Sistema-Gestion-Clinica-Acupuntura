# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Consulta, Paciente
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'index.html')

@login_required
@csrf_exempt
def ListarConsultas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente =paciente_id)
    consultas = Consulta.objects.filter(id_paciente=paciente_id)
    return render(request,'Vistas_Consulta/HistorialConsultas.html',{
        'consultas': consultas,
        'paciente': paciente,
    })

@login_required
@csrf_exempt
def NuevaConsulta(request, paciente_id):
    
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    if request.method == 'POST':
        
        # obtenemos los datos del formulario
        fecha_consulta = request.POST['consulta_fecha']
        motivo_consulta = request.POST['motivo_consulta']
        observacion_consulta = request.POST['observacion_consulta']
        hora_consulta = request.POST['hora_consulta']
        
        # Creamos la nueva consulta para el paciente
        consulta = Consulta.objects.create(
            id_paciente=paciente,
            consulta_fecha=fecha_consulta,
            motivo_consulta=motivo_consulta,
            observacion_consulta=observacion_consulta,
            hora_consulta=hora_consulta,
        )
        
        # Generamos la URL correcta usando reverse
        url = reverse('DetallesConsulta', kwargs={'paciente_id': paciente_id, 'consulta_id': consulta.id_consulta})
        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
    
    return render(request, 'Vistas_Consulta/NuevaConsulta.html', {'paciente': paciente})
           

@login_required
@csrf_exempt
def DetallesConsulta(request, paciente_id, consulta_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    consulta = get_object_or_404(Consulta, pk=consulta_id, id_paciente=paciente)

    fecha_consulta_str = consulta.consulta_fecha.strftime('%d/%B/%Y')

    return render(request, 'Vistas_Consulta/DetallesConsulta.html', {
        'consulta': consulta,
        'paciente': paciente,
        'fecha_consulta_str': fecha_consulta_str,
    })

@login_required
@csrf_exempt
def EditarConsulta(request, paciente_id, consulta_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    consulta = get_object_or_404(Consulta, id_consulta=consulta_id, id_paciente=paciente)
    
    if request.method == 'POST':
        
        # Obtenemos los datos del formulario
        fecha_consulta = request.POST['consulta_fecha']
        motivo_consulta = request.POST['motivo_consulta']
        observacion_consulta = request.POST['observacion_consulta']
        hora_consulta = request.POST['hora_consulta']
        
        # Actualizamos los campos de la consulta existente
        consulta.consulta_fecha = fecha_consulta
        consulta.motivo_consulta = motivo_consulta
        consulta.observacion_consulta = observacion_consulta
        consulta.hora_consulta = hora_consulta
        consulta.save()
        
        # Generamos la URL correcta usando reverse
        url = reverse('DetallesConsulta', kwargs={'paciente_id': paciente_id, 'consulta_id': consulta_id})
        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
    
    return render(request, 'Vistas_Consulta/EditarConsulta.html', {'paciente': paciente, 'consulta': consulta})

@login_required
@csrf_exempt
def EliminarConsulta(request, paciente_id, consulta_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    consulta = get_object_or_404(Consulta, id_consulta=consulta_id, id_paciente=paciente)

    if request.method == 'POST':
        consulta.delete()
        # Redirigir al usuario a la página de lista de consultas o cualquier otra página que desees mostrar después de eliminar la consulta
        return redirect('ListarConsultas', paciente_id=paciente_id)
    
    return render(request, 'Vistas_Consulta/EliminarConsulta.html', {'paciente': paciente, 'consulta': consulta})
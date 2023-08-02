from django.shortcuts import render
# Create your views here.
from Pacientes.models import Terapia,Paciente,Consulta
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from django.http import JsonResponse
import base64

@login_required
def ListarTerapias(request, id_paciente):
    paciente = get_object_or_404(Paciente,id_paciente=id_paciente)
    terapias = Terapia.objects.filter(id_consulta__id_paciente=paciente)
    
    return render(request, 'Terapia/HistorialTerapia.html', {'paciente': paciente, 'terapias': terapias})

@login_required
def NuevaTerapia(request):
    if request.method == 'POST':
        # Procesar el formulario enviado
        image_data = request.POST.get('image_data')
        print("Imagen en Base64 recibida:", image_data)
    
        # Guardar los datos en el modelo Terapia vinculándolo a la consulta
        nueva_terapia = Terapia.objects.create(
            id_consulta = Consulta.objects.get(id_consulta='AO08062301C01'),
            observacion_terapia= 'holaaaaa',
            esquema_terapia=image_data
        )
        nueva_terapia.save()
        return redirect('ListarTerapias', id_paciente='AO08062301')

    return render(request, 'Terapia/NuevaTerapia.html')


@login_required
def VerTerapia(request, terapia_id):
    # Obtener la instancia de Terapia con el ID proporcionado
    terapia = get_object_or_404(Terapia, pk=terapia_id)

    # Decodificar la imagen en Base64 para mostrarla en la plantilla
    imagen_marcada_base64 = terapia.esquema_terapia
    context = {
        'terapia': terapia,
        'imagen_marcada_base64': imagen_marcada_base64,
    }
    return render(request, 'Terapia/DetallesTerapia.html', context)

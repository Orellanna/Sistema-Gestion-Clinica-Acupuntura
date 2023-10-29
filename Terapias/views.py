from django.shortcuts import render
# Create your views here.
from Pacientes.models import Terapia,Paciente,Consulta,Inventario
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from django.http import JsonResponse
import base64
from xhtml2pdf import pisa
from django.http import HttpResponseBadRequest

@login_required
def ListarTerapias(request, id_paciente):
    paciente = get_object_or_404(Paciente,id_paciente=id_paciente)
    terapias = Terapia.objects.filter(id_consulta__id_paciente=paciente)
    
    return render(request, 'Terapia/HistorialTerapia.html', {'paciente': paciente, 'terapias': terapias})

@login_required
def NuevaTerapia(request,paciente_id):
    
    consultas = Consulta.objects.filter(id_paciente=paciente_id).order_by('-consulta_fecha')
    paciente = get_object_or_404(Paciente,id_paciente=paciente_id)
    
    if request.method == 'POST':
        # Procesar el formulario enviado
        image_data = request.POST.get('image_data')
        numero_puntos = request.POST.get('numero_puntos')
        
        if numero_puntos and numero_puntos.isdigit():
            numero_puntos = int(numero_puntos)
        else:
            messages.warning(request, "Debe marcar al menos un punto en el esquema")
            return redirect('NuevaTerapia', paciente_id=paciente_id)
        
        observacion_terapia = request.POST['observacion_terapia']
        consulta_terapia= request.POST['consulta_terapia']
        
        #Obtenemos el producto del inventario 
        producto = Inventario.objects.get(id_suministro='A00001')
        
        #le restamos los puntos equivalentes a agujas que se usaron
        producto.cantidad -= numero_puntos
        producto.save()
        
        # Guardar los datos en el modelo Terapia vinculándolo a la consulta
        nueva_terapia = Terapia.objects.create(
            id_consulta = Consulta.objects.get(id_consulta=consulta_terapia),
            observacion_terapia= observacion_terapia,
            esquema_terapia=image_data
        )
        # nueva_terapia.save()
        return redirect('ListarTerapias', id_paciente=paciente_id)

    return render(request, 'Terapia/NuevaTerapia.html',{
        'paciente':paciente,
        'consultas':consultas,
    })


@login_required
def DetallesTerapia(request, terapia_id, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    terapia = get_object_or_404(Terapia, id_terapia=terapia_id, id_consulta__id_paciente=paciente)
    
    imagen_marcada_base64 = terapia.esquema_terapia

    # Decodificar la imagen base64 y convertirla en una URL válida
    imagen_data_uri = imagen_marcada_base64

    context = {
        'terapia': terapia,
        'imagen_data_uri': imagen_data_uri,
        'paciente': paciente,
    }
    return render(request, 'Terapia/DetallesTerapia.html', context)

@login_required
def EliminarTerapia(request, id_paciente, terapia_id):
   
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    terapia = get_object_or_404(Terapia, id_terapia=terapia_id, id_consulta__id_paciente=paciente)
    
    
    if request.method == 'POST':
  
        #Eliminar la Terapia
        terapia.delete()
    
        # Redirigir al usuario a la página de lista de terapias
        messages.success(request, "La terapia se ha eliminado satisfactoriamente")
        return redirect('ListarTerapias', id_paciente=id_paciente)

    return render(request, 'Terapia/EliminarTerapia.html', {'paciente': paciente, 'terapia': terapia,})  

@login_required
def Imprimir_Terapia(request, paciente_id, terapia_id):
    
    # Obtiene los datos del paciente y la terapia
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    terapia = get_object_or_404(Terapia, id_terapia=terapia_id, id_consulta__id_paciente=paciente)

    imagen_marcada_base64 = terapia.esquema_terapia

    # Decodificar la imagen base64 y convertirla en una URL válida
    imagen_data_uri = imagen_marcada_base64
    
    # Obtiene la plantilla HTML
    template = get_template('Reportes/R_Terapia.html') 

    # Contexto de la plantilla
    context = {
        'paciente': paciente,
        'terapia': terapia,
        'imagen_data_uri': imagen_data_uri,
    }

    # Renderiza la plantilla HTML con el contexto
    html = template.render(context)

    # Crea el objeto HttpResponse con el tipo de contenido apropiado para un PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="terapia.pdf"'  

    # Genera el PDF a partir del HTML renderizado
    pisa.CreatePDF(html, dest=response)

    return response 
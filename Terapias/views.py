from django.shortcuts import render
# Create your views here.
from Pacientes.models import Terapia
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
<<<<<<< Updated upstream
def NuevaTerapia(request):
    return render(request,'Terapia/NuevaTerapia.html')
=======
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

@login_required
def generar_reporte_pdf(request, paciente_id, consulta_id):
    # Obtiene los datos del paciente y la consulta
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    consulta = get_object_or_404(Consulta, id_consulta=consulta_id, id_paciente=paciente)

    # Obtiene la plantilla HTML
    template = get_template('Reportes/R_DetallesConsulta.html') 

    # Contexto de la plantilla
    context = {
        'paciente': paciente,
        'consulta': consulta,
    }

    # Renderiza la plantilla HTML con el contexto
    html = template.render(context)

    # Crea el objeto HttpResponse con el tipo de contenido apropiado para un PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_consulta.pdf"'  

    # Genera el PDF a partir del HTML renderizado
    pisa.CreatePDF(html, dest=response)

    return response

def EnConstruccion(request):
    return render(request,'cons.html')
>>>>>>> Stashed changes

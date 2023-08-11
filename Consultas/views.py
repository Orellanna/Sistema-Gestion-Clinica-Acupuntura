# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Consulta, Paciente, Terapia
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib import messages

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def ListarConsultas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente =paciente_id)
    consultas = Consulta.objects.filter(id_paciente=paciente_id)
    return render(request,'Vistas_Consulta/HistorialConsultas.html',{
        'consultas': consultas,
        'paciente': paciente,
    })
    
@login_required
def ListarConsultasDeshabilitadas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente =paciente_id)
    consultas = Consulta.objects.filter(id_paciente=paciente_id, deshabilitado = True)
    return render(request,'Vistas_Consulta/HistorialConsultasDeshabilitadas.html',{
        'consultas': consultas,
        'paciente': paciente,
    })
    
@login_required
def NuevaConsulta(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    if request.method == 'POST':
        
        # Obtenemos los datos del formulario
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
        
        messages.success(request, "La consulta se ha registrado satisfactoriamente")
        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
    
    return render(request, 'Vistas_Consulta/NuevaConsulta.html', {'paciente': paciente})


           
@login_required
def DetallesConsulta(request, paciente_id, consulta_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    consulta = get_object_or_404(Consulta, pk=consulta_id, id_paciente=paciente)

    return render(request, 'Vistas_Consulta/DetallesConsulta.html', {
        'consulta': consulta,
        'paciente': paciente,
    })

@login_required
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
        
        messages.success(request, "La consulta se ha actualizado satisfactoriamente")
        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
    
    return render(request, 'Vistas_Consulta/EditarConsulta.html', {'paciente': paciente, 'consulta': consulta})

@login_required
def EliminarConsulta(request, paciente_id, consulta_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    consulta = get_object_or_404(Consulta, id_consulta=consulta_id, id_paciente=paciente)

    if request.method == 'POST':
        #Deshabilitar la Consulta
        consulta.deshabilitado = True
        consulta.save()
    
        # Redirigir al usuario a la página de lista de consultas o cualquier otra página que desees mostrar después de eliminar la consulta
        messages.success(request, "La consulta se ha eliminado satisfactoriamente")
        return redirect('ListarConsultas', paciente_id=paciente_id)

    return render(request, 'Vistas_Consulta/EliminarConsulta.html', {'paciente': paciente, 'consulta': consulta})   

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

@login_required
def ReactivarConsulta(request, paciente_id, consulta_id):
    
    consulta = get_object_or_404(Consulta, id_consulta=consulta_id)
    
    # Deshabilitar al paciente
    consulta.deshabilitado = False
    consulta.save()

    # Redirigir a la página de gestión de pacientes
    messages.success(request, "La consulta se ha reactivado satisfactoriamente")
    return redirect('ListarConsultasDesabilitadas', paciente_id=paciente_id)

def EnConstruccion(request):
    return render(request,'cons.html')


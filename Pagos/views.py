from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Pago, Pago, Paciente, Consulta, Terapia
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required
def NuevoPago(request):
    return render(request,'Vistas_Pago/NuevoPago.html')

@login_required

def ListarPagos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pagos = Pago.objects.filter(id_consulta__id_paciente=paciente.id_paciente)    
    return render(request, 'Vistas_Pago/HistorialPagos.html', {'paciente': paciente, 'pagos': pagos})

@login_required
def NuevoPago(request, paciente_id):
    consultas = Consulta.objects.filter(id_paciente=paciente_id, pagada=False, deshabilitado=False)  # Obtienen todas las consultas desde la base de datos
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    if request.method == 'POST':
        
        # Obtenemos los datos del formulario
        consulta_id = request.POST['consulta_id']
        monto_pago = request.POST['monto_pago']
        fecha_pago = request.POST['pago_fecha']
        
        # Creamos el nuevo pago para la consulta del paciente
        pago = Pago.objects.create( 
            id_consulta=Consulta.objects.get(id_consulta=consulta_id),
            concepto_pago=Consulta.objects.get(id_consulta=consulta_id).motivo_consulta,
            monto_pago=monto_pago,
            fecha_pago=fecha_pago,
        )
        # Actualizamos el campo 'pagada' de la consulta a True
        consulta_pagada = Consulta.objects.get(id_consulta=consulta_id)
        consulta_pagada.pagada = True
        consulta_pagada.save()
        
        # Generamos la URL correcta usando reverse
        url = reverse('DetallesPago', kwargs={'paciente_id': paciente_id, 'pago_id': pago.id_pago, 'consulta_id': pago.id_consulta.id_consulta})
        messages.success(request, "El pago se ha registrado satisfactoriamente")

        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
    
    return render(request, 'Vistas_Pago/NuevoPago.html', {'paciente': paciente, 'consultas': consultas})


@login_required
def DetallesPago(request, paciente_id, pago_id, consulta_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pago = get_object_or_404(Pago, pk=pago_id)
    consulta = get_object_or_404(Consulta, pk=consulta_id, id_paciente=paciente)
    return render(request, 'Vistas_Pago/DetallesPago.html', {
        'paciente': paciente, 'pago': pago, 'consultas': consulta
    })
    
from django.urls import reverse

@login_required
def EditarPago(request, paciente_id, pago_id):
    consultas = Consulta.objects.filter(id_paciente=paciente_id, deshabilitado=False)
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pago = get_object_or_404(Pago, id_pago=pago_id)

    if request.method == 'POST':
        consulta_id = request.POST['consulta_id']
        monto_pago = request.POST['monto_pago']
        fecha_pago = request.POST['pago_fecha']

        if consulta_id != str(pago.id_consulta.id_consulta):
            # User changed the associated consultation
            consulta_anterior = Consulta.objects.get(id_consulta=pago.id_consulta.id_consulta, deshabilitado=False)
            consulta_anterior.pagada = False
            consulta_anterior.save()

            consulta_nueva = Consulta.objects.get(id_consulta=consulta_id)
            consulta_nueva.pagada = True
            consulta_nueva.save()

            pago.id_consulta = consulta_nueva

        pago.concepto_pago = pago.id_consulta.motivo_consulta
        pago.monto_pago = monto_pago
        pago.fecha_pago = fecha_pago
        pago.save()

        url = reverse('DetallesPago', kwargs={'paciente_id': paciente_id, 'consulta_id': pago.id_consulta.id_consulta, 'pago_id': pago_id})

        messages.success(request, "El pago se ha actualizado satisfactoriamente")
        return redirect(url)

    return render(request, 'Vistas_Pago/EditarPago.html', {'paciente': paciente, 'pago': pago, 'consultas': consultas})


def EliminarPago(request, paciente_id, pago_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pago = get_object_or_404(Pago, id_pago=pago_id)

    if request.method == 'POST':
        # Marcar el pago como eliminado y desvincularlo de la consulta
        consulta = pago.id_consulta
        consulta.pagada = False
        consulta.save()
        pago.delete()
        
        # Redirigir al usuario a la página de historial de pagos u otra página deseada
        messages.success(request, "El pago se ha eliminado satisfactoriamente")
        return redirect('ListarPagos', paciente_id=paciente_id)

    return render(request, 'Vistas_Pago/EliminarPago.html', {'paciente': paciente, 'pago': pago})

@login_required
def Imprimir_Pago(request, paciente_id, pago_id):
    
    # Obtiene los datos del paciente y la terapia
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pago =  get_object_or_404(Pago, id_pago=pago_id, id_consulta__id_paciente=paciente_id)

    # Obtiene la plantilla HTML
    template = get_template('Reportes/R_Pago.html') 

    # Contexto de la plantilla
    context = {
        'paciente': paciente,
        'pago' : pago,
       
    }

    # Renderiza la plantilla HTML con el contexto
    html = template.render(context)

    # Crea el objeto HttpResponse con el tipo de contenido apropiado para un PDF
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'inline; filename="pago.pdf"'  

    # Genera el PDF a partir del HTML renderizado
    pisa.CreatePDF(html, dest=response)

    return response 




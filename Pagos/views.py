from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Pago, Pago, Paciente, Consulta
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
    consultas = Consulta.objects.all()  # Obtienen todas las consultas desde la base de datos
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
    
@login_required
def EditarPago(request, paciente_id, pago_id):
    consultas = Consulta.objects.all()  # Obtienen todas las consultas desde la base de datos
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    pago = get_object_or_404(Pago, id_pago=pago_id)
    
    if request.method == 'POST':
        
        # Obtenemos los datos del formulario

        consulta_id = request.POST['num_consulta']
        monto_pago = request.POST['monto_pago']
        fecha_pago = request.POST['pago_fecha']
        
        # Creamos el nuevo pago para la consulta del paciente

        pago.concepto_pago=Consulta.objects.get(id_consulta=consulta_id).motivo_consulta,
        pago.monto_pago=monto_pago,
        pago.fecha_pago=fecha_pago,
        pago.id_consulta=Consulta.objects.get(id_consulta=consulta_id)
        pago.save()
        
        # Generamos la URL correcta usando reverse
        url = reverse('DetallesPago', kwargs={'paciente_id': paciente_id, 'pago_id': pago_id})
        
        messages.success(request, "El pago se ha actualizado satisfactoriamente")
        
        # Redirigimos al usuario a la URL correcta
        return redirect(url)
    
    return render(request, 'Vistas_Pago/EditarPago.html', {'paciente': paciente, 'pago': pago, 'consultas': consultas})

import datetime
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Cita
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template import Context
@login_required
def CrearCita(request):
    nueva_cita = Cita()  # Inicializamos la variable fuera del bloque if
    
    if request.method == 'POST':
        
        cita_fecha = request.POST['fecha_cita']
        hora_cita = request.POST['horainicio']
        titulo_cita = request.POST['titulo_cita']
        descripcion_cita = request.POST['descripcion_cita']

        nueva_cita.cita_fecha = cita_fecha
        nueva_cita.horainicio = hora_cita
        nueva_cita.descripcion_cita = descripcion_cita
        nueva_cita.titulo_cita = titulo_cita
        #sumar 60 minutos a la hora de inicio
        # Calcular la hora de finalización sumando 60 minutos a la hora de inicio
        hora_inicio = datetime.datetime.strptime(hora_cita, "%H:%M")
        hora_fin_dt = hora_inicio + datetime.timedelta(minutes=60)
        
        nueva_cita.horafin = hora_fin_dt
        if cita_fecha < datetime.datetime.now().strftime("%Y-%m-%d"):
            nueva_cita.estadocita = True
        else:
            if cita_fecha == datetime.datetime.now().strftime("%Y-%m-%d"):
                if hora_cita < datetime.datetime.now().strftime("%H:%M"):
                    nueva_cita.estadocita = True
                else:
                    nueva_cita.estadocita = False
            else:
                nueva_cita.estadocita = False
        
        nueva_cita.save()
        messages.success(request, "La Cita se ha registrado satisfactoriamente")
        url = reverse('VerCita', kwargs={'cita_id': nueva_cita.id_cita})
        return redirect(url)
    
    return render(request, 'Citas/CrearCita.html', {
        'nueva_cita': nueva_cita,
    })
@login_required
def ListarCitas(request):
    citas = Cita.objects.all()
    return render(request,'index.html',{
        'citas': citas,
    })
def VerCita(request, cita_id):
    cita = get_object_or_404(Cita, id_cita=cita_id)
    return render(request, 'Citas/VerCita.html', {
        'cita': cita,
    })
def EditarCita(request, cita_id):
    cita = get_object_or_404(Cita, id_cita=cita_id)  # Cambiar 'id_cita' a 'id'
    
    if request.method == 'POST':
        cita_fecha = request.POST['fechacita']
        hora_cita = request.POST['horainicio']
        titulo_cita = request.POST['titulo_cita']
        descripcion_cita = request.POST['descripcion_cita']
        hora_fin = request.POST['horafin']
        
        cita.cita_fecha = cita_fecha
        cita.horainicio = hora_cita
        cita.descripcion_cita = descripcion_cita
        cita.titulo_cita = titulo_cita
        cita.horafin = hora_fin
        cita.estadocita = False
        cita.save()
        url = reverse('VerCita', kwargs={'cita_id': cita_id})
        messages.success(request, "La Cita se ha actualizado satisfactoriamente")
        return redirect(url)
    
    return render(request, 'Citas/EditarCita.html', {
        'cita': cita,
    })
def EliminarCita(request, cita_id):
    cita = get_object_or_404(Cita, id_cita=cita_id)  # Cambiar 'id_cita' a 'id'
    cita.delete()
    messages.success(request, "La Cita se ha eliminado satisfactoriamente")
    return redirect('HistorialCitas')

def HistorialCitas(request):
    citas = Cita.objects.all()
    return render(request,'Citas/HistorialCitas.html',{
        'citas': citas,
    })
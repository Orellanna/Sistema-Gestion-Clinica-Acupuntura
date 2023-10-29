from datetime import date, datetime
from datetime import timedelta
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Cita, Paciente
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
        import datetime
        fecha_registro = datetime.datetime.now().strftime("%Y-%m-%d")
        
        nueva_cita.fecha_registro = fecha_registro
        nueva_cita.cita_fecha = cita_fecha
        nueva_cita.horainicio = hora_cita
        nueva_cita.descripcion_cita = descripcion_cita
        nueva_cita.titulo_cita = titulo_cita
        #sumar 60 minutos a la hora de inicio
        # Calcular la hora de finalización sumando 60 minutos a la hora de inicio
        import datetime
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
    now = datetime.now()
    end_of_day = now + timedelta(days=1)  # Fin del día actual
    citas_proximas = Cita.objects.filter(cita_fecha__gte=now, cita_fecha__lt=end_of_day).order_by('cita_fecha', 'horainicio')
    
    for cita in citas_proximas:
        cita_fecha_hora = datetime.combine(cita.cita_fecha, cita.horainicio)  # Combina fecha y hora
        if cita_fecha_hora < now:
            cita.estadocita = True
        else:
            cita.estadocita = False
        cita.save()
    
    return render(request, 'index.html', {
        'citas': Cita.objects.all(),
        'citas_proximas': citas_proximas,
    })

def VerCita(request, cita_id):
    cita = get_object_or_404(Cita, id_cita=cita_id)

    now = datetime.now()

    cita_fecha = cita.cita_fecha
    hora_cita = cita.horainicio
    fecha_hora_cita = datetime.combine(cita_fecha, hora_cita)
        
    if fecha_hora_cita < now:
        cita.estadocita = True
    else:
        cita.estadocita = False
        
    cita.save()  # Asegúrate de guardar los cambios en la base de datos
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

@login_required
def Imprimir_Cita(request,  cita_id):
    
    # Obtiene los datos del paciente y la cita
    #paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    cita =  get_object_or_404(Cita, id_cita=cita_id)
 

    # Obtiene la plantilla HTML
    template = get_template('Reportes/R_Cita.html') 

    # Contexto de la plantilla
    context = {
        #'paciente': paciente,
        'cita' : cita,
        
       
    }

    # Renderiza la plantilla HTML con el contexto
    html = template.render(context)

    # Crea el objeto HttpResponse con el tipo de contenido apropiado para un PDF
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'inline; filename="cita.pdf"'  

    # Genera el PDF a partir del HTML renderizado
    pisa.CreatePDF(html, dest=response)

    return response 
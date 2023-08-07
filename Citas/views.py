from django.shortcuts import render
from Pacientes.models import Citas
from django.contrib.auth.decorators import login_required
import base64
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def GestionCitas(request):
    citas = Citas.objects.all()
    
  
            

    return render(request, 'Vistas_Citas/GestionCitas.html', {
        'citas': citas,
    })


@login_required
def IngresarCita(request):
     nueva_cita = Citas()
     return render(request,'Vistas_Citas/IngresarCita.html',{
        'cita' : nueva_cita,
    })
@login_required
def NuevaCita(request):
     nueva_citas = Citas()
     return render(request,'Vistas_Citas/NuevaCita.html',{
        'cita' : nueva_citas,
    })
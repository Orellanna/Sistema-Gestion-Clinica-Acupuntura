# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from Pacientes.models import Consulta, Paciente
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

@csrf_exempt
def ListarConsultas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente =paciente_id)
    consultas = Consulta.objects.filter(id_paciente=paciente_id)
    return render(request,'Vistas_Consulta/HistorialConsultas.html',{
        'consultas': consultas, 
        'paciente': paciente,
    })

@csrf_exempt
def NuevaConsulta(request, paciente_id):
    
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    if request.method == 'POST':
        
        #obtenemos los datos del formulario
        fecha_consulta = request.POST['fecha_consulta']
        motivo = request.POST['motivo']
        obervacion_consulta = request.POST['obervacion_consulta']
        finalizada = request.POST.get('finalizada', False) == 'on'
        
        #Creamos la nueva consulta para el paciente
        consulta = Consulta.objects.create(
            id_paciente = paciente,
            consulta_fecha = fecha_consulta,
            motivo = motivo,
            obervacion_consulta = obervacion_consulta,
            finalizada = finalizada,
        )
        
        #Redirige al usuario a la pagina del historial de consultas del paciente 
        return redirect('Vistas_Consulta/ListarConsultas', paciente_id=paciente_id)
    
    return render(request,'Vistas_Consulta/NuevaConsulta.html',{'paciente': paciente})
           

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
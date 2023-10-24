from Pacientes.models import Paciente
from datetime import date, datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.views.generic import DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@login_required
def HomePage(request):
    contexto = {'usuario':request.user}
    return render(request,'index.html',contexto)

def es_administrador(user):
    return user.groups.filter(name='Administrador').exists()

@login_required
@user_passes_test(es_administrador)
def Administracion(request):
    return render(request,'Administracion/administracion.html')


def Login(request):
  
    if request.method == 'POST':
        name = request.POST.get('user')
        password = request.POST.get('password')
        
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('ListarCitas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('ListarCitas')
    else:
        if request.user.is_authenticated:
            return redirect('ListarCitas')  # Redirige al usuario autenticado a la vista 'panel'
        else:
            return render(request, "Cuentas/login.html",{})
        
        
def cierre_sesion(request):
    logout(request)
    return redirect('login-page')
        

@login_required
@user_passes_test(es_administrador)
def GestionUsuarios(request):
    usuarios = User.objects.all()
    return render(request,'Administracion/GestionUsuarios.html',{
        'usuarios': usuarios,
    })


from django.contrib import messages

@login_required
@user_passes_test(es_administrador)
def NuevoUsuario(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        contraseña = request.POST['password']
        primerNombre = request.POST['firstname']
        primerApellido = request.POST['lastname']
        correo = request.POST['email']
        cargo = request.POST['cargo']
        
        # Verificar si el usuario ya existe
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'El usuario ya está registrado. Intente con otro.')
            
            context = {
                'usuario': usuario,
                'contraseña': contraseña,
                'primerNombre': primerNombre,
                'primerApellido': primerApellido,
                'correo': correo,
                'cargo': cargo,
            }
            return render(request, 'Cuentas/Registro.html', context=context)

        nuevo_usuario = User.objects.create_user(username=usuario, password=contraseña, email=correo, first_name=primerNombre, last_name=primerApellido)
        
        if cargo == "administrador":
            grupo_administrador = Group.objects.get(name='Administrador')
            nuevo_usuario.groups.add(grupo_administrador)
            
        elif cargo == "acupunturista":
            grupo_acupunturista = Group.objects.get(name='Acupunturista')
            nuevo_usuario.groups.add(grupo_acupunturista)
        
        messages.success(request, "El Usuario se ha creado satisfactoriamente")
        return redirect('gestionUsuarios')
    
    return render(request, 'Cuentas/Registro.html')


@login_required
@user_passes_test(es_administrador)
def VerUsuario(request, username):
    usuario = get_object_or_404(User, username=username)
    
    return render(request, 'Administracion/VerUsuario.html', {
        'usuario': usuario,
    })
    

@login_required
@user_passes_test(es_administrador)
def EliminarUsuario(request, username):
    usuario = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        usuario.delete()
        messages.success(request,"El Usuario se ha eliminado satisfactoriamente")
        return redirect('gestionUsuarios')
    
    return render(request, 'Cuentas/eliminarUsuario.html', {'usuario': usuario})

@login_required
@user_passes_test(es_administrador)
def EditarUsuario(request, username):
    usuario = get_object_or_404(User, username=username)
    grupos_usuario = usuario.groups.values_list('name', flat=True)

    if request.method == 'POST':
        if 'password' in request.POST:
            contraseña = request.POST['password']
            usuario.set_password(contraseña)
        primerNombre = request.POST['firstname']
        primerApellido = request.POST['lastname']
        correo = request.POST['email']
        cargo = request.POST['cargo']

        usuario.username = request.POST['username']
        usuario.first_name = primerNombre
        usuario.last_name = primerApellido
        usuario.email = correo
        usuario.save()

        grupos_usuario = usuario.groups.all()

        if cargo == "administrador" and 'Administrador' not in grupos_usuario:
            grupo_administrador = Group.objects.get(name='Administrador')
            usuario.groups.add(grupo_administrador)
        elif cargo == "acupunturista" and 'Acupunturista' not in grupos_usuario:
            grupo_acupunturista = Group.objects.get(name='Acupunturista')
            usuario.groups.add(grupo_acupunturista)
        elif cargo == "":
            usuario.groups.clear()

        messages.success(request, "El Usuario se ha actualizado satisfactoriamente")
        return redirect('gestionUsuarios')

    return render(request, 'Cuentas/editarUsuario.html', {
        'usuario': usuario,
        'grupos_usuario': grupos_usuario
    })
    
@login_required
@user_passes_test(es_administrador)
def ListarPacientesDeshabilitados(request):
    pacientes = Paciente.objects.filter(deshabilitado=True)
    fecha_actual = datetime.today()

    for paciente in pacientes:
        edad= fecha_actual.year - paciente.fechanac_paciente.year
        if fecha_actual.month < paciente.fechanac_paciente.month and fecha_actual.day < paciente.fechanac_paciente.day:
            edad -=1
        elif fecha_actual.month == paciente.fechanac_paciente.month and fecha_actual.day < paciente.fechanac_paciente.day:
            edad -=1
        paciente.edad = edad    
    return render(request,'Administracion/ListarPacientesDeshabilitados.html',{
        'pacientes': pacientes
    })
    
@login_required
@user_passes_test(es_administrador)
def HabilitarPaciente(request, paciente_id):
    
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    # Deshabilitar al paciente
    paciente.deshabilitado = False
    paciente.save()

    # Redirigir a la página de gestión de pacientes
    messages.success(request, "El Paciente se ha habilitado satisfactoriamente")
    return redirect('listarPacientesDeshabilitados')




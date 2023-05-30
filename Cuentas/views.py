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

def Administracion(request):
    return render(request,'Administracion/administracion.html')

def Login(request):
  
    if request.method == 'POST':
        name = request.POST.get('user')
        password = request.POST.get('password')
        
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('index')
    else:
        if request.user.is_authenticated:
            return redirect('index')  # Redirige al usuario autenticado a la vista 'panel'
        else:
            return render(request, "Cuentas/login.html",{})
        
        
def cierre_sesion(request):
    logout(request)
    return redirect('login-page')
        

@login_required
@csrf_exempt
def GestionUsuarios(request):
    usuarios = User.objects.all()
    return render(request,'Administracion/GestionUsuarios.html',{
        'usuarios': usuarios,
    })


@login_required
@csrf_exempt
def NuevoUsuario(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        contraseña = request.POST['password']
        primerNombre = request.POST['firstname']
        primerApellido = request.POST['lastname']
        correo = request.POST['email']
        cargo = request.POST['cargo']
        
        nuevo_usuario = User.objects.create_user(username=usuario, password=contraseña, email=correo, first_name=primerNombre, last_name=primerApellido)
        
        if cargo == "administrador":
            grupo_administrador = Group.objects.get(name='Administrador')
            nuevo_usuario.groups.add(grupo_administrador)
            
        elif cargo == "acupunturista":
            grupo_acupunturista = Group.objects.get(name='Acupunturista')
            nuevo_usuario.groups.add(grupo_acupunturista)
           
        return redirect('gestionUsuarios')
    
    return render(request, 'Cuentas/Registro.html', {})

def VerUsuario(request, username):
    usuario = get_object_or_404(User, username=username)
    
    return render(request, 'Administracion/VerUsuario.html', {
        'usuario': usuario,
    })
    

@login_required
@csrf_exempt
def EliminarUsuario(request, username):
    usuario = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        usuario.delete()
        messages.info(request,"El Usuario se ha eliminado satisfactoriamente")
        return redirect('gestionUsuarios')
    
    return render(request, 'Cuentas/eliminarUsuario.html', {'usuario': usuario})

@login_required
@csrf_exempt
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


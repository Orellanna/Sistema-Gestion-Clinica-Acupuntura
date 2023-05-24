from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


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

def Register(request):
    pass
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

def RegistrarUsuario(request):
    return render(request,'Cuentas/Registro.html')

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
            nuevo_usuario.is_superuser = True
            nuevo_usuario.is_staff = True
        else:
            nuevo_usuario.is_superuser = False
            nuevo_usuario.is_staff = False
        nuevo_usuario.save()
           
        return redirect('gestionUsuarios')
    
    return render(request, 'Cuentas/Registro.html', {})


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
            nuevo_usuario.is_superuser = True
            nuevo_usuario.is_staff = True
        else:
            nuevo_usuario.is_superuser = False
            nuevo_usuario.is_staff = False
        nuevo_usuario.save()
           
        return redirect('gestionUsuarios')
    
    return render(request, 'Cuentas/Registro.html', {})






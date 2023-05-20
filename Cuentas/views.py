from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def HomePage(request):
    contexto = {'usuario':request.user}
    return render(request,'index.html',contexto)

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
        
    return render(request,'Cuentas/login.html')





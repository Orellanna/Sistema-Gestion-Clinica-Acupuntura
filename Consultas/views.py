# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def DetallesConsulta(request):
    return render(request,'DetallesConsulta.html')
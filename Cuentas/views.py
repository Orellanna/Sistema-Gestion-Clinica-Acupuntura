from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy




# Create your views here.
def Login(request):
    return render(request,'login.html')



from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.contrib import messages


@login_required
def Reportes(request):
    return render(request, 'Reportes/reportes.html')

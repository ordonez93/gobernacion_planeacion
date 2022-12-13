from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from ...models import *
import datetime

fecha_now = datetime.datetime.now()

def proyectos(request):
    listar_proyectos = proyectos.objects.all()
    return render(request, 'proyectos.html', {'proyectos': listar_proyectos, "fecha": fecha_now.year})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from ...models import *
import datetime

fecha_now = datetime.datetime.now()

def listar_proyectos(request):
    listar_proyectos = proyectos.objects.all()
    lista_secretarias = secretarias.objects.all()
    lista_revisores = User.objects.all()
    return render(request, 'proyectos\listar_proyectos.html', {'proyectos': listar_proyectos,'secretarias': lista_secretarias, 'revisores': lista_revisores, "fecha": fecha_now.year})
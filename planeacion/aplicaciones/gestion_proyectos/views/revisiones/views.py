from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from ...models import *
import datetime
from django import forms

fecha_now = datetime.datetime.now()
lista_anios = []
anio_actual = fecha_now.year
def llenar_info(request,id):
   for i in range(2000,fecha_now.year+2):
      lista_anios.append(i)

   lista_municipios = municipios.objects.all()
   lista_estados = estados.objects.all()
   info_proyecto = proyectos.objects.filter(id=id)
   lista_sectores = sectores_inversion.objects.all()
   return render(request, 'revisiones/llenar_info.html', {'municipios':lista_municipios, 'stados':lista_estados, 'proyecto':info_proyecto, 'sectores':lista_sectores, 'anios':lista_anios, 'anio_actual':anio_actual})

def crear_sector2(request, id):
   if request.method == 'POST':
      s = request.POST['nombre_sector']
      nuevo_sector = sectores_inversion()
      nuevo_sector.nombre_sector = s
      nuevo_sector.save()
      (messages.success(request, 'Sector de inverción creado con exito!'))
      return  redirect(to=llenar_info, id=id)
   else:
      (messages.error(request, 'la solictitud no se pudo enviar'))
      return  redirect(to=llenar_info, id=id)

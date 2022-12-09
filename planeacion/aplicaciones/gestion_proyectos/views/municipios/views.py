from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.contrib import messages
from ...models import *
import datetime
# Create your views here.
fecha_now = datetime.datetime.now()


def inicio(request):
    return render(request, 'layout.html', {"fecha": fecha_now.year})


def listar_municipio(request):
    lista_municipios = municipios.objects.all()
    return render(request, 'municipios\listar_municipios.html', {'municipios': lista_municipios, "fecha": fecha_now.year})


def crear_municipio(request):
    if request.method == 'POST':
        m = request.POST['nombre_municipio']
        nuevo_municipio = municipios()
        nuevo_municipio.nombre_municipio = m
        nuevo_municipio.save()
        messages.success(request, 'municipio creado con exito!')
        return redirect(to=listar_municipio)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_municipio)


def editar_municipio(request):
    try:
        if request.method == 'POST':
            id_municipio = request.POST['id_municipio']
            nuevo_nombre = request.POST['nuevo_nombre']
            municipio = municipios.objects.get(id=id_municipio)
            municipio.nombre_municipio = nuevo_nombre
            municipio.save()
            messages.success(request, 'municipio editado con exito!')
            return redirect(to=listar_municipio)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_municipio)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_municipio)

   


def eliminar_municipio(request, id_municipio):
    municipio = municipios.objects.get(id=id_municipio)
    municipio.delete()
    messages.success(request, 'municipio eliminado con exito!')
    return redirect(to=listar_municipio)

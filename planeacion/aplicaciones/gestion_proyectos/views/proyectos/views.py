from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from ...models import *
import datetime
from django import forms

class proyectosForm(forms.ModelForm):
    
    class Meta:
        model = proyectos
        fields = '__all__'

fecha_now = datetime.datetime.now()

def nuevo_proyecto(request):
    listar_secretarias = secretarias.objects.all()
    return render(request, 'proyectos\crear_proyecto.html', {'secretarias': listar_secretarias})

def crear_proyecto(request):
    if request.method == 'POST':
        bpin= request.POST['bpin']
        nombre_proyecto = request.POST['nombre_proyecto']
        fecha_ingreso = request.POST['fecha_ingreso']
        presentacion = request.POST['presentacion']
        secretaria = request.POST['secretaria']
        print(bpin, nombre_proyecto, fecha_ingreso, presentacion, secretaria )
        return redirect(to=nuevo_proyecto)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=nuevo_proyecto)



def listar_proyectos(request):
    
    data={
        'form': proyectosForm()        
    }
    #listar_proyectos = proyectos.objects.all()
    return render(request, 'proyectos\listar_proyectos.html', data)
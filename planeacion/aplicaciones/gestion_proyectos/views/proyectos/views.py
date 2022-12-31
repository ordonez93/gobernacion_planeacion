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
        try:  
            bpin= request.POST['bpin']
            nombre_proyecto = request.POST['nombre_proyecto']
            fecha_ingreso = request.POST['fecha_ingreso']
            presentacion = request.POST['presentacion']
            secretaria = secretarias.objects.get(id=int(request.POST['secretaria']))
            n_proyecto =  proyectos()
            n_proyecto.bpin = bpin
            n_proyecto.nombre_proyecto = nombre_proyecto
            n_proyecto.fecha_ingreso = fecha_ingreso
            n_proyecto.presentacion = presentacion
            n_proyecto.secretaria = secretaria
            n_proyecto.save()
            messages.success(request, 'Se ha creado el proyecto exitosamente')
            return redirect(to=listar_proyectos)
        except:
            messages.error(request, 'Verifique los datos ingresados, el registro no se pudo crear')
            return redirect(to=nuevo_proyecto)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_proyectos)

def ver_estados(request,bpin,id):
    listar_estados = estados_proyectos.objects.filter(proyecto=id)
    return render(request, 'proyectos\prueba_formatos.html', {'estados': listar_estados,'bpin': bpin})

def listar_proyectos(request):
    lista_proyectos = proyectos.objects.all()
    
    return render(request, 'proyectos\listar_proyectos.html', {'proyectos': lista_proyectos})
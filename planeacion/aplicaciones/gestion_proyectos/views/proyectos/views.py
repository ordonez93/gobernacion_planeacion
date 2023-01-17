from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from ...models import *
import datetime
from django import forms


class proyectosForm(forms.ModelForm):

    class Meta:
        model = proyectos
        fields = '__all__'


fecha_now = datetime.datetime.now()

# crud de proyectos

def listar_proyectos(request):
    listar_estados = estados_proyectos.objects.all()
    lista_proyectos = proyectos.objects.all()
    proyectos_por_usuario = usuarios_proyectos.objects.all()
    return render(request, 'proyectos\listar_proyectos.html', {'proyectos': lista_proyectos, 'estados': listar_estados, 'proyecto_usuario': proyectos_por_usuario})


def nuevo_proyecto(request):
    listar_secretarias = secretarias.objects.all()
    return render(request, 'proyectos\crear_proyecto.html', {'secretarias': listar_secretarias})


def crear_proyecto(request):
    if request.method == 'POST':
        try:
            bpin = request.POST['bpin']
            nombre_proyecto = request.POST['nombre_proyecto']
            fecha_ingreso = request.POST['fecha_ingreso']
            presentacion = request.POST['presentacion']
            secretaria = secretarias.objects.get(id=int(request.POST['secretaria']))
            n_proyecto = proyectos()
            n_proyecto.bpin = bpin
            n_proyecto.nombre_proyecto = nombre_proyecto
            n_proyecto.fecha_ingreso = fecha_ingreso
            n_proyecto.presentacion = presentacion
            n_proyecto.secretaria = secretaria
            n_proyecto.save()
            # Crear el estado del proyecto
            ultimo_proyecto = proyectos.objects.latest('id')
            n_estado = estados_proyectos()
            n_estado.proyecto = ultimo_proyecto
            n_estado.estado = estados.objects.get(id=1)
            n_estado.save()
            # Crear el usuario del proyecto
            n_usuario_proyecto = usuarios_proyectos()
            n_usuario_proyecto.proyecto = ultimo_proyecto
            n_usuario_proyecto.usuario = User.objects.get(id=2)
            n_usuario_proyecto.fecha_asignacion = fecha_ingreso
            n_usuario_proyecto.save()
            messages.success(request, 'Se ha creado el proyecto exitosamente')
            return redirect(to=listar_proyectos)
        except:
            messages.error(
                request, 'Verifique los datos ingresados, el registro no se pudo crear')
            return redirect(to=nuevo_proyecto)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_proyectos)


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from ...models import *
import datetime
from django import forms

fecha_now = datetime.datetime.now()

def ver_asignados(request):
    lista_proyectos = proyectos.objects.all()
    proyectos_por_usuario = usuarios_proyectos.objects.all()
    return render(request, 'proyectos\proyecto_usuario.html', {'proyectos': lista_proyectos, 'proyecto_usuario': proyectos_por_usuario})

def cantidad_asignaciones(request, id):
    cantidad = usuarios_proyectos.objects.filter(usuario_id=id).count()
    if cantidad == 0:
        data = {'cantidad': cantidad}
    else:
        data = {'cantidad': cantidad}
    return JsonResponse(data)


def nuevo_asignar(request, id):
    fecha = fecha_now.strftime("%Y-%m-%d")
    proyecto_usuario = []
    listar_proyectos = proyectos.objects.filter(id=id)
    listar_usuarios = User.objects.all()
    proyectos_por_usuario = usuarios_proyectos.objects.all()
    for usuario_contenido in proyectos_por_usuario:
        for usuario in listar_usuarios:
            if usuario_contenido.usuario_id == usuario.id:
                proyecto_usuario.append(usuario.id)

    listar_courrencias = []
    for usuario in listar_usuarios:
        if usuario.id == 2 in proyecto_usuario:
            listar_courrencias.append(
                'Hay '+str(proyecto_usuario.count(usuario.id))+' Proyectos sin asignar')
        else:
            listar_courrencias.append(
                usuario.username+' tiene '+str(proyecto_usuario.count(usuario.id))+' proyectos asignados')
    return render(request, 'asignaciones\proyecto_asignar.html', {'proyecto': listar_proyectos, 'usuarios': listar_usuarios, 'ocurrencias': listar_courrencias, 'fecha': fecha})


def asignar_proyecto(request):

    try:
        if request.method == 'POST':
            proyecto = request.POST['id_proyecto']
            usuario = request.POST['id_usuario']
            fecha = request.POST['fecha']
            if usuario == '2':
                messages.warning(request, 'Debe seleccionar un usuario')
                return redirect(to=ver_asignados)
            else:   
                asignacion = usuarios_proyectos.objects.get(proyecto_id=proyecto)
                asignacion.usuario = User.objects.get(id=usuario)
                asignacion.fecha_asignacion = fecha
                asignacion.save()
                print(proyecto)
                print(usuario)
                print(fecha)
                messages.success(request, 'Asignacion exitosa')
                return redirect(to=ver_asignados)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=ver_asignados)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=ver_asignados)
    
def listar_asignaciones(request):
    lista_proyectos = proyectos.objects.all()
    proyectos_por_usuario = usuarios_proyectos.objects.all()
    return render(request, 'asignaciones\listar_asignaciones.html', {'proyectos': lista_proyectos, 'proyecto_usuario': proyectos_por_usuario})

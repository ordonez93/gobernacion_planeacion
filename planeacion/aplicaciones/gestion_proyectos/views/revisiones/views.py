from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from ...models import *
from aplicaciones.gestion_proyectos.views.tablas.views import *
import datetime


fecha_now = datetime.datetime.now()
lista_anios = []
anio_actual = fecha_now.year

def listar_revisiones(request):
   lista_revisiones = revisiones.objects.all()
   lista_proyectos = proyectos.objects.all()
   proyectos_estados = estados_proyectos.objects.all()
   lista_estados = estados.objects.all()
   return render(request, 'revisiones/listar_revisiones.html', {'revisiones':lista_revisiones, 'proyectos':lista_proyectos, 'estados':lista_estados, 'proyectos_estados':proyectos_estados})

def nueva_revision(request,id):
   try:
      if proyecto_archivo.objects.filter(proyecto=id).exists():
         proyecto = proyectos.objects.get(id=id)
         estados_pro = estados_proyectos.objects.all()
         for e in estados_pro:
            if e.proyecto_id ==id:
               estado_id = e.estado_id
               estado = estados.objects.get(id=estado_id)
               estado = estado.nombre_estado
         lista_estados = estados.objects.all()
         return render(request, 'revisiones/revisiones.html', {'proyectos':proyecto, 'estados':lista_estados, 'estado':estado})
      else:
         messages.info(request, 'Primero debe llenar todos los campos para la información del proyecto')
         return redirect(to=llenar_info,id=id)
   except:
      messages.error(request, 'error al cargar el proyecto')
      return redirect(to=inicio)
      
def llenar_info(request,id):
   for i in range(2000,fecha_now.year+2):
      lista_anios.append(i)
   lista_municipios = municipios.objects.all()
   lista_estados = estados.objects.all()
   id=id
   info_proyecto = proyectos.objects.filter(id=id)
   lista_sectores = sectores_inversion.objects.all()
   return render(request, 'revisiones/llenar_info.html', {'municipios':lista_municipios, 'stados':lista_estados, 'proyecto':info_proyecto, 'sectores':lista_sectores, 'anios':lista_anios, 'anio_actual':anio_actual, 'id':id})

def guardar_info(request):
   if request.method =='POST':
      try:
         proyecto = proyectos.objects.get(id=int(request.POST['id_proyecto']))
         id=proyecto.id
         #secretaria = secretarias.objects.get(id=int(request.POST['secretaria']))
         id_plataforma = request.POST['id_plataforma']
         vigencia = request.POST['vigencia']
         valor= request.POST['valor']
         municipio = municipios.objects.get(id=int(request.POST['municipio']))
         sector = sectores_inversion.objects.get(id=int(request.POST['sector']))
         info_proyecto = proyecto_archivo()
         info_proyecto.proyecto = proyecto
         info_proyecto.identificador = id_plataforma
         info_proyecto.vigencia = vigencia
         info_proyecto.valor_proyecto = valor
         info_proyecto.municipio = municipio
         info_proyecto.sector = sector
         info_proyecto.save()
         messages.success(request, 'informacion del Proyecto creada con exito!')
         return redirect(to=nueva_revision, id=id)
      except:
         messages.error(request, 'la solictitud no se pudo enviar, verifica los campos')
         return redirect(to=nueva_revision, id=id)

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

def crear_revision(request):
 
      if request.method == 'POST': 
         fecha_revision = fecha_now.strftime("%Y-%m-%d")
         proyecto = proyectos.objects.get(id=int(request.POST['proyecto_id']))
         estado_anterior = request.POST['estado_anterior']
         detalle_revision = request.POST['detalle_revision']
         revisor = request.POST['revisor']
         revision = revisiones()
         if request.FILES:
            archivo_revision = request.FILES['archivo_revision']
            revision.archivo_revision = archivo_revision
         revision.fecha_revision = fecha_revision
         revision.proyecto = proyecto
         revision.estado_anterior = estado_anterior
         revision.detalle_revision = detalle_revision
         revision.revisor = revisor
         revision.save()
         #editar estado del proyecto
         estado = estados.objects.get(id=int(request.POST['estado']))
         estado_proyecto = estados_proyectos.objects.get(proyecto_id=proyecto)
         estado_proyecto.estado = estado
         estado_proyecto.proyecto = proyecto
         estado_proyecto.save()
         #editar usuario del proyecto
         usuario = User.objects.get(id=2)
         usuario_proyecto = usuarios_proyectos.objects.get(proyecto_id=proyecto)
         usuario_proyecto.usuario = usuario
         usuario_proyecto.proyecto = proyecto
         usuario_proyecto.save()
         messages.success(request, 'Revision creada con exito!')
         return redirect(to=listar_revisiones)
      else:
         messages.error(request, 'la solictitud no se pudo enviar')
         return redirect(to=listar_revisiones)


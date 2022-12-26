from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from ...models import *
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
fecha_now = datetime.datetime.now()


def tablas(request):
    contarMunicipios = municipios.objects.all().count()
    contarSecretarias = secretarias.objects.all().count()
    contarSectores = sectores_inversion.objects.all().count()
    contarEstados = estados_proyectos.objects.all().count()
    return render(request, 'tablas\menutablas.html', {"fecha": fecha_now.year, "contarMunicipios": contarMunicipios, "contarSecretarias": contarSecretarias, "contarSectores": contarSectores, "contarEstados": contarEstados})


def inicio(request):
    lista_notas = notas.objects.all()
    return render(request, 'inicio.html', {"fecha": fecha_now.year, 'notas':  lista_notas})

# funciones de municipios ----------------------------------------------


def listar_municipio(request):
    lista_municipios = municipios.objects.all()
    return render(request, 'tablas\listar_municipios.html', {'municipios': lista_municipios, "fecha": fecha_now.year})


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
            id_municipio = request.POST['id_editar']
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


def eliminar_municipio(request):
    try:
        if request.method == 'POST':
            id_municipio = request.POST['id_eliminar']
            municipio = municipios.objects.get(id=id_municipio)
            municipio.delete()
            messages.success(request, 'municipio eliminado con exito!')
            return redirect(to=listar_municipio)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_municipio)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_municipio)

# funciones de secreatarias ------------------------------------------------


def listar_secretarias(request):
    lista_secretarias = secretarias.objects.all()
    return render(request, 'tablas\listar_secretarias.html', {'secretarias':  lista_secretarias, "fecha": fecha_now.year})


@permission_required('gestion_proyectos.add_secretarias')
def crear_secretaria(request):
    try:
        if request.method == 'POST':
            s = request.POST['nombre_secretaria']
            nueva_secretaria = secretarias()
            nueva_secretaria.nombre_secretaria = s
            nueva_secretaria.save()
            messages.success(request, 'Secretaría creada con exito!')
            return redirect(to=listar_secretarias)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_secretarias)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_secretarias)

@permission_required('gestion_proyectos.change_secretarias')
def editar_secretaria(request):
    try:
        if request.method == 'POST':
            id_secretaria = request.POST['id_editar']
            nuevo_nombre = request.POST['nuevo_nombre']
            secretaria = secretarias.objects.get(id=id_secretaria)
            secretaria.nombre_secretaria = nuevo_nombre
            secretaria.save()
            messages.success(request, 'secretaría editada con exito!')
            return redirect(to=listar_secretarias)
        else:
            messages.error(request, 'Error en autenticación')
            return redirect(to=listar_secretarias)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_secretarias)

@permission_required('gestion_proyectos.delete_secretarias')
def eliminar_secretaria(request):
    try:
        if request.method == 'POST':
            id_secretaria = request.POST['id_eliminar']
            secretaria = secretarias.objects.get(id=id_secretaria)
            secretaria.delete()
            messages.success(request, 'secretaria eliminada con exito!')
            return redirect(to=listar_secretarias)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_secretarias)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_secretarias)

# funciones de sectores de inversion ------------------------------------------------


def listar_sectores(request):
    lista_sectores = sectores_inversion.objects.all()
    return render(request, 'tablas\listar_sectores.html', {'sectores':  lista_sectores, "fecha": fecha_now.year})


def crear_sector(request):
    if request.method == 'POST':
        s = request.POST['nombre_sector']
        d = request.POST['descripcion_sector']
        nuevo_sector = sectores_inversion()
        nuevo_sector.nombre_sector = s
        nuevo_sector.descripcion = d
        nuevo_sector.save()
        messages.success(request, 'Sector de inverción creado con exito!')
        return redirect(to=listar_sectores)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_secretarias)


def editar_sector(request):
    try:
        if request.method == 'POST':
            id_sector = request.POST['id_editar']
            nuevo_nombre = request.POST['nuevo_nombre']
            descripcion = request.POST['nueva_descripcion']
            sector = sectores_inversion.objects.get(id=id_sector)
            sector.nombre_sector = nuevo_nombre
            sector.descripcion = descripcion
            sector.save()
            messages.success(request, 'Sector de inversión editado con exito!')
            return redirect(to=listar_sectores)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_sectores)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_sectores)


def eliminar_sector(request):
    try:
        if request.method == 'POST':
            id_sector = request.POST['id_eliminar']
            sector = sectores_inversion.objects.get(id=id_sector)
            sector.delete()
            messages.success(
                request, 'Sector de inversión eliminado con exito!')
            return redirect(to=listar_sectores)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_sectores)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_sectores)

# funciones de estados para proyectos ------------------------------------------------


def listar_estados(request):
    lista_estados = estados_proyectos.objects.all()
    return render(request, 'tablas\listar_estados.html', {'estados':  lista_estados, "fecha": fecha_now.year})


def crear_estado(request):
    if request.method == 'POST':
        e = request.POST['nombre_estado']
        d = request.POST['descripcion_estado']
        nuevo_estado = estados_proyectos()
        nuevo_estado.nombre_estado = e
        nuevo_estado.descripcion = d
        nuevo_estado.save()
        messages.success(request, 'Estado  para proyecto creado con exito!')
        return redirect(to=listar_estados)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_estados)


def editar_estado(request):
    try:
        if request.method == 'POST':
            id_estado = request.POST['id_editar']
            nuevo_nombre = request.POST['nuevo_nombre']
            descripcion = request.POST['nueva_descripcion']
            estado = estados_proyectos.objects.get(id=id_estado)
            estado.nombre_estado = nuevo_nombre
            estado.descripcion = descripcion
            estado.save()
            messages.success(
                request, 'Estado para proyecto editado con exito!')
            return redirect(to=listar_estados)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_estados)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_estados)


def eliminar_estado(request):
    try:
        if request.method == 'POST':
            id_estado = request.POST['id_eliminar']
            estado = estados_proyectos.objects.get(id=id_estado)
            estado.delete()
            messages.success(
                request, 'Estado para proyecto eliminado con exito!')
            return redirect(to=listar_estados)
        else:
            messages.error(request, 'la solicitud no se pudo enviar')
            return redirect(to=listar_estados)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=listar_estados)


def crear_nota(request):
    if request.method == 'POST':
        n = request.POST['mensaje_nota']
        nueva_nota = notas()
        nueva_nota.nombre_nota = n
        nueva_nota.save()
        #messages.success(request, 'Nota creada con exito!')
        return redirect(to=inicio)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=inicio)


def eliminar_nota(request, id_nota):
    try:
        nota = notas.objects.get(id=id_nota)
        nota.delete()
        return redirect(to=inicio)
    except NameError:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=inicio)

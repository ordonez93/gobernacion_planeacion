from django.urls import path
from aplicaciones.gestion_proyectos.views.municipios.views import *
urlpatterns = [
    path('', inicio, name="inicio"),

    #rutas para la gestion de municipios
    path('listar_municipios/', listar_municipio,name='listar_municipios'),
    path('nuevo_municipio/', crear_municipio,name='nuevo_municipio'),
    path('editar_municipio/<int:id_municipio>/', editar_municipio,name='editar_municipio'),
    path('eliminar_municipio/<int:id_municipio>/', eliminar_municipio,name='eliminar_municipio'),

    #rutas para la gestion de secretarías


    #rutas para la gestion de sectores de inversión



]
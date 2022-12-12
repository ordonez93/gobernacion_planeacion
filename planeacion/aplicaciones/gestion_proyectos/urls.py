from django.urls import path
from aplicaciones.gestion_proyectos.views.tablas.views import *
urlpatterns = [
    path('', inicio, name="inicio"),

    #rutas para la gestion de municipios
    path('listar_municipios/', listar_municipio,name='listar_municipios'),
    path('nuevo_municipio/', crear_municipio,name='nuevo_municipio'),
    path('editar_municipio/', editar_municipio,name='editar_municipio'),
    path('eliminar_municipio/', eliminar_municipio,name='eliminar_municipio'),
    path('tablas/', tablas,name='tablas'),

    #rutas para la gestion de secretarías


    #rutas para la gestion de sectores de inversión



]
from django.urls import path
from aplicaciones.gestion_proyectos.views.tablas.views import *
from aplicaciones.gestion_proyectos.views.login.views import *
from aplicaciones.gestion_proyectos.views.proyectos.views import *
urlpatterns = [

    # rutas de inicio y tablas
    path('', inicio, name="inicio"),
    path('tablas/', tablas,name='tablas'),

    #rutas para la gestion de municipios
    path('listar_municipios/', listar_municipio,name='listar_municipios'),
    path('nuevo_municipio/', crear_municipio,name='nuevo_municipio'),
    path('editar_municipio/', editar_municipio,name='editar_municipio'),
    path('eliminar_municipio/', eliminar_municipio,name='eliminar_municipio'),
    

    #rutas para la gestion de secretarías
    path('listar_secretarias/', listar_secretarias,name='listar_secretarias'),
    path('nueva_secretaria/', crear_secretaria,name='nueva_secretaria'),
    path('editar_secretaria/', editar_secretaria,name='editar_secretaria'),
    path('eliminar_secretaria/', eliminar_secretaria,name='eliminar_secretaria'),

    #rutas para la gestion de sectores de inversión
    path('listar_sectores/', listar_sectores,name='listar_sectores'),
    path('nuevo_sector/', crear_sector,name='nueva_secretaria'),
    path('editar_sector/', editar_sector,name='editar_sector'),
    path('eliminar_sector/', eliminar_sector,name= 'eliminar_sector'),

    #rutas para la gestion de estados de proyectos
    path('listar_estados/', listar_estados,name='listar_estados'),
    path('nuevo_estado/', crear_estado,name='nuevo_estado'),
    path('editar_estado/', editar_estado,name='editar_estado'),
    path('eliminar_estado/', eliminar_estado,name='eliminar_estado'),

    #rutas de notas
    path('crear_nota/', crear_nota,name='nueva_nota'),
    path('eliminar_nota/<int:id_nota>', eliminar_nota,name='eliminar_nota'),

    #login
    path('/acounts/login', login,name='login'),

    #rutas proyectos
    path('listar_proyectos/', listar_proyectos,name='listar_proyectos'),
]
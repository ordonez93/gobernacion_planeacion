from django.urls import path
from aplicaciones.gestion_proyectos.views import *
urlpatterns = [
    path('', inicio),
]
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(municipios)
admin.site.register(secretarias)
admin.site.register(sectores_inversion)
admin.site.register(estados)
admin.site.register(estados_proyectos)
admin.site.register(proyectos)
admin.site.register(usuarios_proyectos)
admin.site.register(revisiones)
admin.site.register(proyecto_archivo)
admin.site.register(notas)


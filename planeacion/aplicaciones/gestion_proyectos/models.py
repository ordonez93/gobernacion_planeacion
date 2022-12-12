from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class municipios(models.Model):
    nombre_municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, default='Activo')
    def __str__(self):
        return self.nombre_municipio

class secretarias(models.Model):
    nombre_secretaria = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, default='Activo')
    def __str__(self):
        return self.nombre_secretaria

class sectores_inversion(models.Model):
    nombre_sector = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=50, default='Activo')
    def __str__(self):
        return self.nombre_sector

class estados_proyectos(models.Model):
    nombre_estado = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre_estado

class proyectos(models.Model):
    numero_proyecto = models.CharField(max_length=200,unique=True)
    nombre_proyecto = models.TextField()
    fecha_inicio = models.DateField()
    valor_proyecto = models.DecimalField(max_digits=15, decimal_places=2)
    municipio = models.ForeignKey(municipios, on_delete=models.CASCADE)
    secretaria = models.ForeignKey(secretarias, on_delete=models.CASCADE)
    sector = models.ForeignKey(sectores_inversion, on_delete=models.CASCADE)
    estado = models.ForeignKey(estados_proyectos, on_delete=models.CASCADE)
    archivo_proyecto = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.nombre_proyecto


class asignar_proyectos(models.Model):
    fecha_asignacion = models.DateField()
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)    
    detalle = models.TextField( null=True, blank=True)
    archivo_asignado = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.proyecto.nombre_proyecto



class revisiones(models.Model):
    fecha_cambio = models.DateField()
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=70)
    nuevo_estado = models.CharField(max_length=70)
    detalle_revision = models.TextField( null=False, blank=True)
    archivo_revision = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.proyecto.nombre_proyecto


    
    

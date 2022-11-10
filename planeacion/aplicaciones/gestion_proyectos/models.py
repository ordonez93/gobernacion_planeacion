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
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, default='Activo')
    def __str__(self):
        return self.nombre_sector

class estados_proyectos(models.Model):
    nombre_estado = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre_estado

class proyectos(models.Model):
    numero_proyecto = models.CharField(max_length=200)
    nombre_proyecto = models.TextField()
    fecha_inicio = models.DateField()
    valor_proyecto = models.DecimalField(max_digits=15, decimal_places=2)
    municipio = models.ForeignKey(municipios, on_delete=models.CASCADE)
    secretaria = models.ForeignKey(secretarias, on_delete=models.CASCADE)
    sector = models.ForeignKey(sectores_inversion, on_delete=models.CASCADE)
    estado = models.ForeignKey(estados_proyectos, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_proyecto


class asignar_proyectos(models.Model):
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    estado = models.CharField(max_length=50, default='Activo')

class realizar_cambios(models.Model):
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_cambio = models.DateField()
    estado = models.CharField(max_length=50, default='Activo')

    
    

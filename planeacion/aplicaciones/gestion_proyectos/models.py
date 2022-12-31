from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class municipios(models.Model):
    nombre_municipio = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_municipio
    
    class meta:
        verbose_name_plural = 'municipios'
        verbose_name = 'municipio'
        db_table = 'municipios'
        ordering = ['-id']

class secretarias(models.Model):
    nombre_secretaria = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, default='Activo')
    def __str__(self):
        return self.nombre_secretaria
    class meta:
        verbose_name_plural = 'secretarias'
        verbose_name = 'secretaria'
        db_table = 'secretarias'
        ordering = ['-id']

class sectores_inversion(models.Model):
    nombre_sector = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=50, default='Activo')
    def __str__(self):
        return self.nombre_sector
    class meta:
        verbose_name_plural = 'sectores'
        verbose_name = 'sectores'
        db_table = 'sectores_inversion'
        ordering = ['-id']

class estados(models.Model):
    nombre_estado = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nombre_estado
    class meta:
        verbose_name_plural = 'estados_proyectos'
        verbose_name = 'estados_proyectos'
        db_table = 'estados_proyectos'

class proyectos(models.Model):
    bpin = models.CharField(max_length=200,unique=True,null=False,blank=False) # codigo de referencia del proyecto
    nombre_proyecto = models.TextField()
    fecha_ingreso = models.DateField()
    presentacion = models.CharField(max_length=50)
    secretaria = models.ForeignKey(secretarias, on_delete=models.CASCADE)
    #estado = models.ForeignKey(estados, on_delete=models.CASCADE,null=False, blank=False)
    #revisor = models.ForeignKey(User, on_delete=models.CASCADE,null=True)# usuario que revisará el proyecto
    #archivo_proyecto = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.nombre_proyecto
    class meta:
        verbos_name_plural = 'proyectos'
        verbose_name = 'proyecto'
        db_table = 'proyectos'
        ordering = ['-id']



class estados_proyectos(models.Model):
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE)
    estado = models.ForeignKey(estados, on_delete=models.CASCADE)
    def __str__(self):
        return {},{},{},format(self.proyecto.nombre_proyecto,self.estado.nombre_estado)



# por si un proyecto tiene varios usuarios asignados
class usuarios_proyectos(models.Model):
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    #archivo_asignado = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.proyecto.nombre_proyecto


class proyecto_archivo(models.Model):
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE, null=False, blank=False)
    identificador = models.CharField(max_length=200,unique=True) # id del proyecto desde la pagina miga
    vigencia = models.IntegerField(max_length=10, null=False, blank=False)#si la vigencia es diferente al año actual, el se debe guardar como nuevo registro en esta tabla
    valor_proyecto = models.DecimalField(max_digits=15, decimal_places=2)
    municipio= models.ForeignKey(municipios, on_delete=models.CASCADE, null=False, blank=False)
    sector = models.ForeignKey(sectores_inversion, on_delete=models.CASCADE,null=False, blank=False)
    #archivo_proyecto = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.proyecto.nombre_proyecto
    class meta:
        verbose_name_plural = 'proyecto_archivo'
        verbose_name = 'proyecto_archivo'
        db_table = 'proyecto_info'
        ordering = ['-id']


class revisiones(models.Model):
    fecha_revision = models.DateField()
    proyecto = models.ForeignKey(proyectos, on_delete=models.CASCADE, null=False, blank=False)
    estado_anterior = models.CharField(max_length=70)
    detalle_revision = models.TextField( null=False, blank=True)
    archivo_revision = models.FileField(upload_to='static/archivos_proyectos', null=True, blank=True)
    def __str__(self):
        return self.proyecto.nombre_proyecto
    class meta:
        verbose_name_plural = 'revisiones'
        verbose_name = 'revisiones'
        db_table = 'revisiones'
        ordering = ['-id']


class notas(models.Model):
    nombre_nota = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_nota
    class meta:
        verbose_name_plural = 'notas'
        verbose_name = 'notas'
        db_table = 'notas'
        ordering = ['-id']

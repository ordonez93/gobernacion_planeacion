# Generated by Django 4.1.1 on 2022-11-17 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_proyectos', '0006_revisiones_remove_asignar_proyectos_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignar_proyectos',
            name='archivo_asignado',
            field=models.FileField(blank=True, null=True, upload_to='static/archivos_proyectos'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='archivo_proyecto',
            field=models.FileField(blank=True, null=True, upload_to='static/archivos_proyectos'),
        ),
        migrations.AddField(
            model_name='revisiones',
            name='archivo_revision',
            field=models.FileField(blank=True, null=True, upload_to='static/archivos_proyectos'),
        ),
    ]
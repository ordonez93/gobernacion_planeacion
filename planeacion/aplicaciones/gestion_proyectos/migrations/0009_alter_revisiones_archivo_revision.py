# Generated by Django 4.1.1 on 2023-01-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_proyectos', '0008_alter_proyecto_archivo_vigencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisiones',
            name='archivo_revision',
            field=models.FileField(blank=True, null=True, upload_to='archivos_adjuntos/'),
        ),
    ]

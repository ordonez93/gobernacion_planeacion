# Generated by Django 4.1.1 on 2022-12-31 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_proyectos', '0005_usuarios_proyectos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='presentacion',
            field=models.IntegerField(choices=[[0, 'Nuevo'], [1, 'Actualización']], default=0),
        ),
    ]

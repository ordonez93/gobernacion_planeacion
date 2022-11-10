# Generated by Django 4.1.1 on 2022-11-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estados_proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=50)),
                ('estado', models.CharField(default='Activo', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='secretarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_secretaria', models.CharField(max_length=50)),
                ('estado', models.CharField(default='Activo', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sectores_inversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sector', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(default='Activo', max_length=50)),
            ],
        ),
    ]

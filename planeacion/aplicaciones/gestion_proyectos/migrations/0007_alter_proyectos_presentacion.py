# Generated by Django 4.1.1 on 2022-12-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_proyectos', '0006_alter_proyectos_presentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='presentacion',
            field=models.CharField(max_length=50),
        ),
    ]
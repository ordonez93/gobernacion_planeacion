# Generated by Django 4.1.1 on 2022-11-17 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_proyectos', '0005_alter_proyectos_numero_proyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='revisiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cambio', models.DateField()),
                ('estado_anterior', models.CharField(max_length=70)),
                ('nuevo_estado', models.CharField(max_length=70)),
                ('detalle_revision', models.TextField(blank=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_proyectos.proyectos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='asignar_proyectos',
            name='estado',
        ),
        migrations.AddField(
            model_name='asignar_proyectos',
            name='detalle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='realizar_cambios',
        ),
    ]

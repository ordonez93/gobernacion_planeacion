# Generated by Django 4.1.1 on 2023-01-17 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_proyectos', '0014_alter_revisiones_archivo_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisiones',
            name='revisor',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]

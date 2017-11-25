# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fechaP', models.DateTimeField(verbose_name='fecha de publicacion')),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='novedad',
            name='fechaP',
            field=models.DateTimeField(verbose_name='fecha de publicacion'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20171126_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigacion',
            name='archivo',
            field=models.FileField(blank=True, upload_to='web/uploads/%Y/%m/%d/'),
        ),
    ]

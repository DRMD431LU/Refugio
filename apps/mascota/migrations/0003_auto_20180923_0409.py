# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-23 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20180923_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, null=True, to='mascota.Vacuna'),
        ),
    ]

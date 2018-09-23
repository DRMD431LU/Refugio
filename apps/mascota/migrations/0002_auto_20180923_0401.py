# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-23 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(to='mascota.Vacuna'),
        ),
    ]

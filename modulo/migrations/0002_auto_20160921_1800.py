# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.Area'),
        ),
    ]

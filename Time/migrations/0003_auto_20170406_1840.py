# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Time', '0002_auto_20170329_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]

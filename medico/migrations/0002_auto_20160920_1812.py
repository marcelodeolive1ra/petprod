# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]

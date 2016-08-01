# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 21:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='codigo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]

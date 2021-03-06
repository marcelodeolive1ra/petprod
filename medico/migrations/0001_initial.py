# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-13 16:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('perfil', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('salario', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('expertise', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('atendimento', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('pontualidade', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
            ],
        ),
    ]

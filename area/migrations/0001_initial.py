# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
    ]

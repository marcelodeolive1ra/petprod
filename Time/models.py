from django.db import models
from django.core.validators import MinValueValidator
from django import forms
from .validator import validate_blank

# Create your models here.



class Time(models.Model):
    id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=20)
    login = models.CharField(max_length=15, validators=[validate_blank])
    senha = models.CharField(max_length=20)
    caixa = models.FloatField()




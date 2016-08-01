from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Medico(models.Model):
    classificacao = ((1,'1'),(2,'2'),(3,'3'))
    id = models.AutoField(u'id', primary_key=True, unique=True, default=1)
    perfil = models.IntegerField(validators=[MinValueValidator(1)])
    salario = models.FloatField(validators=[MinValueValidator(0.0)])
    expertise = models.IntegerField(default=1, choices=classificacao)
    atendimento = models.IntegerField(default=1, choices=classificacao)
    pontualidade = models.IntegerField(default=1, choices=classificacao)
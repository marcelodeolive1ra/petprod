from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Evento(models.Model):

    id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=200)

    entrada = models.FloatField(validators=[MinValueValidator(0.0)])
    desvio_padrao = models.FloatField(validators=[MinValueValidator(0.0)])

    preco_atendimento = models.FloatField(validators=[MinValueValidator(0.0)])
    nivel_especialidade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    nivel_tecnologia = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    media_conforto = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    velocidade_atendimento = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])


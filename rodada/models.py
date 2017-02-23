from django.db import models
from django.core.validators import MinValueValidator
from evento.models import Evento

class Rodada (models.Model):
    class Meta:
        verbose_name = 'rodada'
        verbose_name_plural = 'rodadas'

    numeroRodada = models.IntegerField(validators=[MinValueValidator(1)])
    duracao = models.IntegerField(validators=[MinValueValidator(1)])
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)
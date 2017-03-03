from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from area.models import Area


class Evento(models.Model):
    #class Meta:
     #   abstract = True
    nome = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    #entrada da classe social
    entradaA = models.FloatField(validators=[MinValueValidator(0)])
    entradaB = models.FloatField(validators=[MinValueValidator(0)])
    entradaC = models.FloatField(validators=[MinValueValidator(0)])
    entradaD = models.FloatField(validators=[MinValueValidator(0)])
    entradaE = models.FloatField(validators=[MinValueValidator(0)])

    desvioA = models.FloatField(validators=[MinValueValidator(0)])
    desvioB = models.FloatField(validators=[MinValueValidator(0)])
    desvioC = models.FloatField(validators=[MinValueValidator(0)])
    desvioD = models.FloatField(validators=[MinValueValidator(0)])
    desvioE = models.FloatField(validators=[MinValueValidator(0)])
'''
class Evento_Customizavel(Evento):
    customizavel = models.BooleanField(default=True)

class Evento_Default(Evento):
    default = models.BooleanField(default=True)
'''
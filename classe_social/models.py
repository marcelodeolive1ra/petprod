from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Classe_Social(models.Model):
    classificacao = ((1, '1'), (2, '2'), (3, '3'))
    id = models.AutoField(u'id', primary_key=True, unique=True, default=1)
    nome = models.CharField(max_length=200)
    preco_atendimento = models.FloatField(validators=[MinValueValidator(0.0)])
    nivel_especialidade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    nivel_tecnologia = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    media_conforto = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    velocidade_atendimento = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])

from django.db import models
from django.core.validators import MinValueValidator
# from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

class Modulo(models.Model):
    class Meta:
        unique_together = (('codigo', 'nome'),)
        #TODO adicionar mensagem de erro

    id = models.AutoField(u'id', primary_key=True, unique=True)
    classificacao = ((1, '1'), (2, '2'), (3, '3'))
    codigo = models.IntegerField(validators=[MinValueValidator(1)])
    nome = models.CharField(max_length=200)
    custo_de_aquisicao = models.FloatField(validators=[MinValueValidator(0.0)])
    custo_mensal = models.FloatField(validators=[MinValueValidator(0.0)])
    tecnologia = models.IntegerField(default=1, choices=classificacao)
    conforto = models.IntegerField(default=1, choices=classificacao)
    capacidade = models.IntegerField(validators=[MinValueValidator(1)])
    preco_do_tratamento = models.FloatField(validators=[MinValueValidator(0.0)])

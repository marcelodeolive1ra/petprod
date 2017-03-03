from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from classe_social.models import Classe_Social
from area.models import Area_ClasseSocial


class Evento(models.Model):
    id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=200)




class Evento_ModificaEntrada(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    area_classe_social = models.ForeignKey(Area_ClasseSocial, on_delete=models.CASCADE)
    modificadorEntrada = models.FloatField(validators=[MinValueValidator(0)])
    modificadorDesvio = models.FloatField(validators=[MinValueValidator(0)])


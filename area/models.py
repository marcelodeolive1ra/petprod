from django.db import models
from django.core.validators import MinValueValidator
from classe_social.models import Classe_Social

class Area(models.Model):
    id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Area_ClasseSocial(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    classe_social = models.ForeignKey(Classe_Social, on_delete=models.CASCADE)
    entrada = models.IntegerField(validators=[MinValueValidator(1)])
    desvios = models.IntegerField(validators=[MinValueValidator(0)])





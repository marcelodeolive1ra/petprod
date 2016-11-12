from django.db import models

class Cenario(models.Model):
    id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=200)

from django.db import models

class Area(models.Model):

    id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome
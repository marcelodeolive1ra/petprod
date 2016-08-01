from django.db import models
from django.core.validators import MinValueValidator

class Emprestimo(models.Model):
    valor = models.FloatField(validators=[MinValueValidator(1.0)])

# Create your models here.

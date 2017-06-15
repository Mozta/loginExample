from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Lista(models.Model):
    matricula = models.IntegerField()
    nombre = models.CharField(max_length=200)
    ult_periodo = models.CharField(max_length=200)
    tutor = models.CharField(max_length=200)
    avance = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return self.nombre

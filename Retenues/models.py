from django.db import models


# Create your models here.
class Retenues(models.Model):
    # idRetenue
    intitule = models.CharField(max_length=100, null=True, blank=True)

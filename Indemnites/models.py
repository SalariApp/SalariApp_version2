from django.db import models


# Create your models here.
class Indemnites(models.Model):
    # idIndemnite
    intitule = models.CharField(max_length=50, null=True)

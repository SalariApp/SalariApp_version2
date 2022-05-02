from django.db import models
from Entreprise.models import Entreprise


# Create your models here.
class Adresse(models.Model):
    # idAdresse
    typeAdresse = models.CharField(max_length=50, null=True)
    entreprise = models.ForeignKey(Entreprise, null=True, on_delete=models.CASCADE)

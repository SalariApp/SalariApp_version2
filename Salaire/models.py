from django.db import models
from Employe.models import Employe


# Create your models here.
class Salaire(models.Model):
    # idSalaire
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    satutSalaire = models.IntegerField
    employe = models.ForeignKey(Employe, null=True, on_delete=models.CASCADE)

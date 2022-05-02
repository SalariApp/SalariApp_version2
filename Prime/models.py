from django.db import models


# Create your models here.
class Prime(models.Model):
    ETAT = (('Retirée', 'Retirée'),
            ('Pas retirée', 'Pas retirée'))
    # idPrime
    etat = models.CharField(max_length=50, null=True, choices=ETAT, blank=True)
    typePrime = models.CharField(max_length=50, null=True)
    valeur = models.IntegerField(null=True)

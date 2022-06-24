from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save


class Entreprise(models.Model):
    identifiant = models.OneToOneField(User, on_delete=models.CASCADE, related_name='entreprise')
    FORMEJURIDIQUE = (('SCS', 'SCS'),
                      ('SNC', 'SNC'),
                      ('SARL', 'SARL'),
                      ('SA', 'SA'),
                      ('SAS', 'SAS'),
                      ('GIE', 'GIE'),
                      ('SEP', 'SEP'),
                      ('SCP', 'SCP'),
                      ('SCI', 'SCI'),
                      ('SP', 'SP'))
    nomEntreprise = models.CharField(default='Entreprise', max_length=50, null=True, blank=True)
    anneeCreation = models.DateField(null=True)
    activite = models.CharField(default='Activité', max_length=100, null=True, blank=True)
    effectif = models.IntegerField(default=10, null=True, blank=True)
    capital = models.IntegerField(default=10000, null=True, blank=True)
    nomDirecteur = models.CharField(default='Directeur', max_length=50, null=True, blank=True)
    numeroContribuable = models.IntegerField(default=5, null=True, blank=True)
    formeJuridique = models.CharField(default='SARL', max_length=50, null=True, choices=FORMEJURIDIQUE, blank=True)
    chiffreAffaire = models.IntegerField(default=10000, null=True, blank=True)
    image = models.ImageField('Label', upload_to='cars', null=True)

    def __str__(self):
        return self.nomEntreprise


def create_user(sender, instance, created, **Kwargs):
    if created:
        Entreprise.objects.create(identifiant=instance)


def save_user(sender, instance, **Kwargs):
    instance.entreprise.save()


post_save.connect(create_user, sender=User)
post_save.connect(save_user, sender=User)

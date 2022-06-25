from django.contrib.auth.models import User
from django.db import models
# from Salaire.models import Salaire
from Entreprise.models import Entreprise


# Create your models here.
class Employe(models.Model):
    NATIONALITE = (('Allemande', 'Allemande'),
                   ('Algérienne', 'Algérienne'),
                   ('Angolaise', 'Angolaise'),
                   ('Argentine', 'Argentine'),
                   ('Américaine', 'Américaine'),
                   ('Anglaise', 'Anglaise'),
                   ('Australienne', 'Australienne'),
                   ('Autrichienne', 'Autrichienne'),
                   ('Bahamienne', 'Bahamienne'),
                   ('Belge', 'Belge'),
                   ('Béninoise', 'Béninoise'),
                   ('Bisseau-Guinéene', 'Bisseau-Guinéene'),
                   ('Brésilienne', 'Brésilienne'),
                   ('Burkinabé', 'Burkinabé'),
                   ('Burundi', 'Burundi'),
                   ('Camerounaise', 'Camerounaise'),
                   ('Canadienne', 'Canadienne'),
                   ('cap-verdienne', 'cap-verdienne'),
                   ('Chilienne', 'Chilienne'),
                   ('Chinoise', 'Chinoise'),
                   ('Colombienne', 'Colombienne'),
                   ('Congolaise', 'Congolaise'),
                   ('Corée du sud', 'Corée du sud'),
                   ('Coréene', 'Coréene'),
                   ('Cubaine', 'Cubaine'),
                   ('Danoise', 'Danoise'),
                   ('Egyptienne', 'Egyptienne'),
                   ('Equatorienne', 'Equatorienne'),
                   ('Espagnole', 'Espagnole'),
                   ('Estonienne', 'Estonienne'),
                   ('Etyiopienne', 'Etyiopienne'),
                   ('Finlandaise', 'Finlandaise'),
                   ('Française', 'Française'),
                   ('Gabonaise', 'Gabonaise'),
                   ('gambienne', 'gambienne'),
                   ('ghanéene', 'ghanéene'),
                   ('Greque', 'Greque'),
                   ('Guinéenne', 'Guinéenne'),
                   ('Haïtienne', 'Haïtienne'),
                   ('Hongroise', 'Hongroise'),
                   ('Indienne', 'Indienne'),
                   ('Indonésienne', 'Indonésienne'),
                   ('Irlandaise', 'Irlandaise'),
                   ('Islandaise', 'Islandaise'),
                   ('Israélienne', 'Israélienne'),
                   ('Italienne', 'Italienne'),
                   ('Ivoirienne', 'Ivoirienne'),
                   ('Jamaïquaine', 'Jamaïquaine'),
                   ('Japonaise', 'Japonaise'),
                   ('Jordanienne', 'Jordanienne'),
                   ('Kényene', 'Kényene'),
                   ('Libye', 'Libye'),
                   ('Marocaine', 'Marocaine'),
                   ('Mexicaine', 'Mexicaine'),
                   ('Motswanan', 'Motswanan'),
                   ('Mozambique', 'Mozambique'),
                   ('Namibie', 'Namibie'),
                   ('Nigeria', 'Nigeria'),
                   ('Nigérienne', 'Nigérienne'),
                   ('Norvégienne', 'Norvégienne'),
                   ('Pakistanaise', 'Pakistanaise'),
                   ('Palestinienne', 'Palestinienne'),
                   ('Péruvienne', 'Péruvienne'),
                   ('Philippine', 'Philippine'),
                   ('Polonaise', 'Polonaise'),
                   ('Portugaise', 'Portugaise'),
                   ('Québécoise', 'Québécoise'),
                   ('Roumaine', 'Roumaine'),
                   ('Russe', 'Russe'),
                   ('Sénégalaise', 'Sénégalaise'),
                   ('Suédoise', 'Suédoise'),
                   ('Tchadienne', 'Tchadienne'),
                   ('Tchèque', 'Tchèque'),
                   ('Tunisienne', 'Tunisienne'),
                   ('Vietnamienne', 'Vietnamienne'),
                   ('Zambienne', 'Zambienne'),
                   ('Zimbabwéenne', 'Zimbabwéenne'))
    STATUSMATRIMONIAL = (('Marié(e)', 'Marié(e)'),
                         ('Célibataire', 'Célibataire'),
                         ('Divorsé(e)', 'Divorsé(e)'))
    TYPECONTRAT = (('Durée déterminée', 'Durée déterminée'),
                   ('Durée indéterminée', 'Durée indéterminée'))
    SEXE = (('Maxculin', 'Maxculin'),
            ('Féminin', 'Féminin'))

    identifiantUser = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='employé')
    # idEntreprise = models.ForeignKey(Entreprise, null=True, on_delete=models.CASCADE, related_name='employé')
    nomEmploye = models.CharField(max_length=50, null=True)
    prenomEmploye = models.CharField(max_length=50, null=True)
    dateNaissance = models.DateField(null=True)
    lieuNaissance = models.CharField(max_length=50, null=True)
    nationalite = models.CharField(max_length=50, null=True, choices=NATIONALITE)
    statusMatrimonial = models.CharField(max_length=50, null=True, choices=STATUSMATRIMONIAL)
    fonction = models.CharField(max_length=50, null=True)
    typeContrat = models.CharField(max_length=50, null=True, choices=TYPECONTRAT)
    dateRecrutement = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    salaireBase = models.IntegerField(null=True)
    salaireNet = models.IntegerField(null=True)
    sexe = models.CharField(max_length=10, null=True, choices=SEXE)

    def __str__(self):
        return self.nomEmploye

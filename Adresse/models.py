from django.db import models
from Entreprise.models import Entreprise


# Create your models here.
class Adresse(models.Model):
    # idAdresse
    TYPEADRESSE = (('Adresse mail', 'Adresse mail'),
                   ('Téléphone', 'Téléphone'),
                   ('Site Internet', 'Site Internet'),
                   ('Boite postale', 'Boite postale'),
                   ('Pays', 'Pays'),
                   ('Ville', 'Ville'),
                   ('Quartier', 'Quartier'),
                   ('Inplantation', 'Inplantation'),
                   ('Fax', 'Fax'))
    typeAdresse = models.CharField(max_length=50, null=True, choices=TYPEADRESSE)
    valeur = models.CharField(max_length=50, null=True)

    entreprise = models.ForeignKey(Entreprise, null=True, on_delete=models.CASCADE)

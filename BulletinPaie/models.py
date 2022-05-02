from django.db import models
from Employe.models import Employe


# Create your models here.
class BulletinPaie(models.Model):
    # idBulletinPaie
    employe = models.ForeignKey(Employe, null=True, on_delete=models.RESTRICT)

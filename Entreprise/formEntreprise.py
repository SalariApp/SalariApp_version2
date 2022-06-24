from django.forms import ModelForm
from django import forms

from .models import Entreprise


class FormulaireEntreprise(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = [
            'nomEntreprise',
            'activite',
            'anneeCreation',
            'effectif',
            'capital',
            'nomDirecteur',
            'numeroContribuable',
            'chiffreAffaire',
            'formeJuridique',
            'image',
        ]

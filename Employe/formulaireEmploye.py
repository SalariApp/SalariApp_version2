from django import forms

from Employe.models import Employe


class FormulaireEmploye(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nomEmploye',
                  'prenomEmploye',
                  'dateNaissance',
                  'lieuNaissance',
                  'sexe',
                  'nationalite',
                  'statusMatrimonial',
                  'fonction',
                  'typeContrat',
                  'dateRecrutement',
                  'dateFin',
                  'salaireBase'
                  ]

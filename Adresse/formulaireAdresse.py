from django import forms

from Adresse.models import Adresse


class FormulaireAdresse(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['typeAdresse',
                  'valeur']

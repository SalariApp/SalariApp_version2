from django import forms

from Indemnites.models import Indemnites


class FormulaireIndemnites(forms.ModelForm):
    class Meta:
        model = Indemnites
        exclude = ['employe'
                  ]
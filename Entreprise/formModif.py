# from django.forms import ModelForm
from django import forms

from .models import Entreprise


class FormulaireEntrepriseM(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'

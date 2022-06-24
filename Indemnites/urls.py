from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('AjoutIndem/<int:cle>', views.Ajoute_Indemnites, name='AjoutIndem'),
    path('InfoIndem', views.Affiche_Indemnites, name='InfoIndem')
]

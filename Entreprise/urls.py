from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Connexion, name='Login'),
    path('Dash', views.Dash, name='Dash'),
    path('inscrit', views.Inscription, name='inscrit'),
    path('Erreur', views.Erreur, name='Erreur'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('creerEntre', views.AjoutEntrepise, name='creerEntre'),
    path('infoEntre', views.InfoEntreprise, name='infoEntre'),

]

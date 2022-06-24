from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('AjoutA', views.Ajoute_Adresse, name='AjoutA')
]

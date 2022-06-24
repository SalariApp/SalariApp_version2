from django.contrib import admin
from django.urls import path
from . import views
from Adresse.views import Ajoute_Adresse

urlpatterns = [
    path('CreerEmploye', views.Ajoute_Employe, name='CreerEmploye'),
    path('InfoE', views.Liste_Employe, name='InfoE'),
    path('modifier/<int:employe_id>', views.modifiemploye, name='ModifierEmploye'),
    path('<int:employe_id>', views.Supprime_Employe, name='supp'),
    path('EmployeMenu', views.EmployeMenu, name='EmployeMenu'),
]

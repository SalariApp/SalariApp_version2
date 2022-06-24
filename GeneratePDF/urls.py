from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('pdf', views.pdfEmploye, name='pdf'),
    path('pdf1', views.pdfEntreprie, name='pdf1')
]

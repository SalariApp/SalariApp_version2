from django.shortcuts import render

from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.deprecation import *
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.contrib import messages
from ProjetSalariApp import settings


def Login(request):
    return render(request, "Entreprise/Login/Inscription.html")


def Dash(request):
    return render(request, "Entreprise/Dashboard/Dash.html")

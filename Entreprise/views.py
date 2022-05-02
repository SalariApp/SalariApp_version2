from Tools.scripts import generate_token

from Entreprise.formEntreprise import FormulaireEntreprise
from Entreprise.models import Entreprise
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.deprecation import *
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from Entreprise.tokens import generate_token
from django.contrib.auth.models import User
from django.contrib import messages
from ProjetSalariApp import settings

# from .formModif import FormulaireEntrepriseM
# from .models import Entreprise
# from .formEntreprise import FormulaireEntreprise
from lib2to3.fixes.fix_input import context


def Valid(request):
    return render(request, 'Entreprise/Validation.html')


def Erreur(request):
    return render(request, 'Erreur.html')


# ================================================Inscription=====================================================

def Inscription(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,
                           "Ce nom d'utilisateur exite déjà, veillez reéssayez avec un autre nom s'il vous plaît")
            return redirect('inscrit')

        if not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit comporter les caractères alpha-Numerique!")
            return redirect('inscrit')

        if User.objects.filter(email=email):
            messages.error(request,
                           "Cette adresse email exite déjà, veillez reéssayez avec une autre Email s'il vous plaît")
            return redirect('inscrit')

        if pass1.isalnum() and len(pass1) < 8:
            messages.error(request,
                           "Pour des mesures de sécurité, votre mot de passe doit contenir des caractères spéciaux (&#{[|@=+$£*!?) "
                           "et doit etre constituer d'au moins 8 caractères")
            return redirect('inscrit')

        if pass1 != pass2:
            messages.error(request, "Les deux mot de passe doivent être identique!")
            return redirect('inscrit')

        myuser = User.objects.create_superuser(username, email, pass1)
        myuser.first_name = username
        myuser.is_active = True
        myuser.save()

        messages.error(request,
                       "Votre compte a été crée avec succès. Un message de confirmation a été envoyé dans votre boite Email, veillez le confirmer pour activer votre compte")

        try:
            # Bienvenue Email

            subject = "Bienvenue dans SalariApp !!"
            message = "Hello " + myuser.first_name + "!! \n" + "Merci pour avoir choisi SalariApp pour la gestion de vos salaires \nVous allez recevoir un message de confirmation pour activer votre compte. \n\n\n Merci \n Cordialement SalariApp "
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            # Addresse Email de confirmation

            current_site = get_current_site(request)
            email_subject = "Confirmation de l'addresse email"
            message2 = render_to_string('Entreprise/Login/Email_confirm.html', {
                'name': myuser.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email]
            )
            email.fail_silently = True
            email.send()
        except:
            messages.error(request, "Erreur de l'envoie de l'email, verifier votre connexion "
                                    "et si le problème insiste, veiller contacter vortre administrateur ")

        return redirect('Login')

    return render(request, "Entreprise/Login/Inscription.html")


# ================================================FIN=====================================================

# =========================================Activation_du_compte============================================


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('Login')
    else:
        return render(request, 'Entreprise/Login/Activation_echoué.html')


# ================================================FIN=====================================================


# ================================================Connexion=====================================================

def Connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if pass1 != pass2:
            messages.error(request, "Erreur de mot de passe!")
            return redirect('Login')

        if user is not None:
            login(request, user)
            # fname = user.first_name
            return redirect('Dash')
        # render(request, "Entreprise/Dashboard/Dash.html", {'fname': fname})
        else:
            messages.error(request, "Erreur de connexion, veillez entrer les informations correctes")
            return redirect('Login')

    return render(request, "Entreprise/Login/Connexion.html")


# ====================================================FIN==========================================================

def Dash(request):
    return render(request, "Entreprise/Dashboard/Dash.html")


# ================================================ Entreprise =====================================================

# ================================================ Ajout_entreprise ================================================


def AjoutEntrepise(request):
    monformEntreprise = FormulaireEntreprise()
    user = request.user
    entreprise = Entreprise.objects.get(identifiant=user)
    if request.method == 'POST':
        monformEntreprise = FormulaireEntreprise(request.POST, request.FILES, instance=entreprise)
        print(1)
        if monformEntreprise.is_valid():
            print(2)
            entreprise.nomEntreprise = monformEntreprise.cleaned_data.get('nomEntreprise')
            entreprise.activite = monformEntreprise.cleaned_data.get('activite')
            entreprise.adresse = monformEntreprise.cleaned_data.get('adresse')
            entreprise.anneeCreation = monformEntreprise.cleaned_data.get('anneeCreation')
            entreprise.effectif = monformEntreprise.cleaned_data.get('effectif')
            entreprise.capital = monformEntreprise.cleaned_data.get('capital')
            entreprise.chiffreAffaire = monformEntreprise.cleaned_data.get('chiffreAffaire')
            entreprise.nomDirecteur = monformEntreprise.cleaned_data.get('nomDirecteur')
            entreprise.numeroContribuable = monformEntreprise.cleaned_data.get('numeroContribuable')
            entreprise.formeJuridique = monformEntreprise.cleaned_data.get('formeJuridique')
            entreprise.save()
            return redirect('Dash')
    context = {'monformEntreprise': monformEntreprise}
    return render(request, 'Entreprise/AjoutEntre.html', context)


@login_required
def InfoEntreprise(request):
    user = request.user
    entreprises = Entreprise.objects.get(identifiant=user)
    context = {'entreprises': entreprises}
    return render(request, 'Entreprise/InfoEntreprise.html', context)


def Entreprisek(request):
    try:
        entreprises = Entreprise.objects.all()
        for element in entreprises:
            print(element.nomEntreprise)
    except:
        a = False
    else:
        a = True
    context = {'cle': entreprises}
    return render(request, 'Entreprise/Entreprise.html', context)


def modifientreprise(request, entreprise_id):
    entreprise = get_object_or_404(Entreprise, id=entreprise_id)
    dic = {'nomEntreprise': entreprise.nomEntreprise,
           'adresse': entreprise.adresse,
           'anneeCreation': entreprise.anneeCreation,
           'activite': entreprise.activite,
           'effectif': entreprise.effectif,
           'capital': entreprise.capital,
           'nomDirecteur': entreprise.nomDirecteur,
           'numeroContribuable': entreprise.numeroContribuable,
           'formeJuridique': entreprise.formeJuridique,
           'chiffreAffaire': entreprise.chiffreAffaire}

    form_em = FormulaireEntrepriseM(data=dic)
    if request.method == 'POST':
        form_em = FormulaireEntrepriseM(request.POST, instance=entreprise)
        if form_em.is_valid():
            form_em.save()
            return redirect('entreprise')
    if request.method == 'GET':
        form_em = FormulaireEntrepriseM(data=dic)
    return render(request, 'Entreprise/modifEntreprise.html', {'modifientreprise': form_em})


def Entreprisek(request):
    try:
        entreprises = Entreprise.objects.all()
        for element in entreprises:
            print(element.nomEntreprise)
    except:
        a = False
    else:
        a = True
    context = {'cle': entreprises}
    return render(request, 'Entreprise/Entreprise.html', context)


# ================================================EXTRA=====================================================
@login_required
def Parametre(request):
    return render(request, 'Parametre.html')


@login_required
def Apropos(request):
    return render(request, 'Apropos.html')


@login_required
def Contact(request):
    return render(request, 'Contact.html')


@login_required
def Aide(request):
    return render(request, 'Aide.html')


# ====================================================FIN=====================================================


# =====================================================DECONEXION==========================================
@login_required
def Finish(request):
    logout(request)
    return redirect('login')

# ==========================================================================================================

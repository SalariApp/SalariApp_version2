from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
import Indemnites
from Employe.models import Employe
from Indemnites.formulaireIndemnites import FormulaireIndemnites
from Indemnites.models import Indemnites


def Ajoute_Indemnites(request, cle):
    monformIndemnites = FormulaireIndemnites()
    emp = Employe.objects.get(id=cle)
    print(4)
    if request.method == 'POST':
        monformIndemnites = FormulaireIndemnites(request.POST)
        print(3)
        if monformIndemnites.is_valid():
            print(2)
            intitule = monformIndemnites.cleaned_data.get('intitule')
            valeur = monformIndemnites.cleaned_data.get('valeur')
            if valeur < 0:
                messages.error(request, 'Entrez une valeur positive')
                return redirect('AjoutIndem', cle)
            type = monformIndemnites.cleaned_data.get('type')
            indemnites = Indemnites.objects.filter(employe=emp)
            print(indemnites)
            for element in indemnites:
                print(element)
                if element.intitule == intitule and element.valeur == valeur and element.type == type:
                    messages.error(request, 'Cette indemnité existe déjà')
                    return redirect('AjoutIndem', cle)
            if type == 'Valeur fixe':
                idem = Indemnites.objects.create(intitule=intitule, valeur=valeur, type=type, employe=emp)
                print('reussi')
                return redirect('InfoIndem')
            if type == 'pourcentage sur salaire':
                if valeur > 100:
                    messages.error(request, 'Entrez un pourcentage entre 0 et 100')
                    return redirect('AjoutIndem', cle)
                idem = Indemnites.objects.create(intitule=intitule, valeur=valeur, type=type, employe=emp)
                print('reussi')
                return redirect('InfoIndem')
    context = {'monformIndemnites': monformIndemnites}
    return render(request, 'Salaire/Indemnites.html', context)


def Affiche_Indemnites(request):
    print(1)
    Indemnitess = Indemnites.objects.all()
    print(2)
    context2 = {'Indemnitess': Indemnitess}
    print(3)
    return render(request, 'Indemnites/AfficherIndemnites.html', context2)

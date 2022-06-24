from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from Adresse.formulaireAdresse import FormulaireAdresse
from django.contrib import messages

from Adresse.models import Adresse
from Entreprise.models import Entreprise


@login_required(login_url='Login')
def Ajoute_Adresse(request):
    monformAdresse = FormulaireAdresse()
    print(4)
    if request.method == 'POST':
        user = request.user
        ent = Entreprise.objects.get(identifiant=user)
        monformAdresse = FormulaireAdresse(request.POST)
        print(3)
        if monformAdresse.is_valid():
            print(2)
            type = request.POST.get('typeAdresse')
            val = request.POST.get('valeur')
            #user = User.objects.get(id=id_user)
            print(7)
            adresse = Adresse.objects.filter(entreprise=ent)
            for element in adresse:
                if element.typeAdresse == type and element.valeur == val:
                    messages.error(request, 'Cette adresse existe déjà')
                    return redirect('AjoutA')
            print('reussi')
            ad = Adresse.objects.create(typeAdresse=request.POST.get('typeAdresse'), valeur=request.POST.get('valeur'), entreprise=ent)
            return redirect('AjoutA')
        print(1)
    context = {'monformAdresse': monformAdresse}
    return render(request, 'Adresse/AjouterAdresse.html', context)



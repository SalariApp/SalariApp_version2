from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.randomtext import objects

from Employe.formulaireEmploye import FormulaireEmploye
from Employe.models import Employe
from Entreprise.models import Entreprise


@login_required(login_url='Login')
def EmployeMenu(request):
    return render(request, 'Employe/EmployeMenu.html')


@login_required(login_url='Login')
def Ajoute_Employe(request):
    monformEmploye = FormulaireEmploye()
    user = request.user
    #    employe = Employe.objects.filter(identifiantUser=user)
    print(1)
    if request.method == 'POST':
        monformEmploye = FormulaireEmploye(request.POST, request.FILES)
        print(2)
        if monformEmploye.is_valid():
            print(3)
            nom = monformEmploye.cleaned_data.get('nomEmploye')
            nom = monformEmploye.cleaned_data.get('prenomEmploye')
            nom = monformEmploye.cleaned_data.get('dateNaissance')
            nom = monformEmploye.cleaned_data.get('lieuNaissance')
            nom = monformEmploye.cleaned_data.get('sexe')
            nom = monformEmploye.cleaned_data.get('nationalite')
            nom = monformEmploye.cleaned_data.get('statusMatrimonial')
            nom = monformEmploye.cleaned_data.get('fonction')
            nom = monformEmploye.cleaned_data.get('typeContrat')
            nom = monformEmploye.cleaned_data.get('dateRecrutement')
            nom = monformEmploye.cleaned_data.get('dateFin')
            nom = monformEmploye.cleaned_data.get('salaireBase')
            print(4)
            monformEmploye.save()
            return redirect('InfoE')
        print(5)
    context = {'monformEmploye': monformEmploye}
    return render(request, 'Employe/Ajouter.html', context)


@login_required(login_url='Login')
def Liste_Employe(request):
    user = request.user
    Employes = Employe.objects.all()
    context2 = {'Employes': Employes}
    k: int = len(Employes)
    print(k)
    return render(request, 'Employe/AfficheEmploye.html', context2)





@login_required(login_url='Login')
def modifiemploye(request, employe_id):
    user = request.user
    employe = get_object_or_404(Employe, pk=employe_id)
    dic = {'nomEmploye': employe.nomEmploye,
           'prenomEmploye': employe.prenomEmploye,
           'dateNaissance': employe.dateNaissance,
           'lieuNaissance': employe.lieuNaissance,
           'sexe': employe.sexe,
           'nationalite': employe.nationalite,
           'statusMatrimonial': employe.statusMatrimonial,
           'fonction': employe.fonction,
           'typeContrat': employe.typeContrat,
           'dateRecrutement': employe.dateRecrutement,
           'dateFin': employe.dateFin,
           'salaireBase': employe.salaireBase,
           }
    form_em = FormulaireEmploye(data=dic)
    if request.method == 'POST':
        form_em = FormulaireEmploye(request.POST, instance=employe)
        if form_em.is_valid():
            form_em.save()
            return redirect('InfoE')
    return render(request, 'Employe/ModifierEmploye.html', {'modifiemploye': form_em})


@login_required(login_url='Login')
def Supprime_Employe(request, employe_id):
    user = request.user
    supprimeur = Employe.objects.get(id=employe_id)
    supprimeur.delete()
    return redirect('InfoE')

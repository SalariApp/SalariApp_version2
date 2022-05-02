from django.shortcuts import render, redirect, get_object_or_404
from Employe.formulaireEmploye import FormulaireEmploye
from Employe.models import Employe
from Entreprise.models import Entreprise


def Ajoute_Employe(request):
    monformEmploye = FormulaireEmploye()
    user = request.user
    employe = Employe.objects.filter(identifiantUser=user)
    print(4)
    if request.method == 'POST':
        monformEmploye = FormulaireEmploye(request.POST, request.FILES)
        print(3)
        if monformEmploye.is_valid():
            print(2)
            monformEmploye.save()
            return redirect('InfoE')
        print(1)
    context = {'monformEmploye': monformEmploye}
    return render(request, 'Employe/Ajouter.html', context)


def Liste_Employe(request):
    user = request.user
    Employes = Employe.objects.filter(identifiantUser=user)
    context2 = {'Employes': Employes}
    return render(request, 'Employe/Afficher.html', context2)


def modifiemploye(request, employe_id):
    user = request.user
    employe = get_object_or_404(Employe, pk=employe_id)
    dic = {'nomEmploye': employe.nomEmploye,
           'prenomEmploye': employe.prenomEmploye,
           'dateNaissance': employe.dateNaissance,
           'lieuNaissance': employe.lieuNaissance,
           'sexe': employe.sexe,
           'nationalite': employe.nationalite,
           'statusMatrimonial': 'Marié(e)',
           'fonction': employe.fonction,
           'typeContrat': employe.typeContrat,
           'dateRecrutement': employe.dateRecrutement,
           'dateFin': employe.dateFin,
           'salaireBase': employe.salaireBase,
           'salaireNet': employe.salaireNet}

    form_em = FormulaireEmploye(data=dic)
    if request.method == 'POST':
        form_em = FormulaireEmploye(request.POST, instance=employe)
        if form_em.is_valid():
            form_em.save()
            return redirect('Modifier')
    if request.method == 'GET':
        form_em = FormulaireEmploye(data=dic)
    return render(request, 'Employe/ModifierEmploye.html', {'modifiemploye': form_em})


def Supprime_Employe(request, employe_id):
    user = request.user
    supprimeur = Employe.objects.get(id=employe_id)
    supprimeur.delete()
    return redirect('Supprimer')


def Modifier(request):
    Employes = Employe.objects.all()
    context2 = {'Employes': Employes}
    # print(Salaire.CalculeSalaireBrut.fget(SalaireBrut))
    return render(request, 'Employe/Modifier.html', context2)


def Supprimer(request):
    Employes = Employe.objects.all()
    context2 = {'Employes': Employes}
    # print(Salaire.CalculeSalaireBrut.fget(SalaireBrut))
    return render(request, 'Employe/Supprimer.html', context2)

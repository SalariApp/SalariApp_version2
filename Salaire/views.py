from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Employe.models import Employe

# Create your views here.


@login_required(login_url='Login')
def Salaire(request):
    user = request.user
    Employes = Employe.objects.all()
    context2 = {'Employes': Employes}
    return render(request, 'Salaire/Salaire.html', context2)

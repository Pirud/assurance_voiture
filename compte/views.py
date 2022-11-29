from django.shortcuts import redirect, render 
from .form  import CreerUtilisateur 
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from adherant.models import adherant
from vehicule.models import vehicule
from sinistre.models import sinistre
from assure.models import assure

def acces(request):# cette fonction(login) consiste à rediriger l'utilisateur vers le tableau de bord apres l'authentification
    nombre_client=adherant.objects.all().count()
    nombre_voiture=vehicule.objects.all().count()
    nombre_sinistre=sinistre.objects.all().count()
    nombre_assurance=assure.objects.all().count()
    context={'nombre_client':nombre_client,'nombre_voiture':nombre_voiture,'nombre_sinistre':nombre_sinistre,'nombre_assurance':nombre_assurance}
    if request.method=='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
           login(request,user) 
           return render(request,'dashboard/dashboard.html',context)
        else:
            messages.info(request,"il ya une erreur dans le nom d'utilsateur et le mot de passe")
    return render(request,'acces/login.html',context)

def inscription(request):# cette fonction(login up) permet à l'utilisateur de creer un compte d'ulisateur
    form=CreerUtilisateur()
    if request.method =='POST':
       form=CreerUtilisateur(request.POST)
       if form.is_valid():
           form.save()
           user=form.cleaned_data.get('username')
           messages.success(request,'le compte a ete creer avec succes pour '+user)
           return render(request,'acces/login.html')
       else:
           messages.info(request,'il y a une erreur')
    context={'form':form}
    return render(request,'inscription/inscription.html',context)


def deconnecter(request): # cette fonction(logout) permet à l'utilisateur de se deconnecter 
    logout(request)
    return render(request,'acces/login.html')
# Create your views here.

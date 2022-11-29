from django.shortcuts import render
from adherant.models import adherant
from vehicule.models import vehicule
from .forms import FormulaireAdherant
from .forms import FormulaireVoiture
from sinistre.models import sinistre
from vehicule.models import vehicule
from assure.models import assure
from .forms import FormulaireAssure
from .forms import FormulaireSinistre
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='compte:acces')#cette focntion consite a rediriger l'utisateur vers l'interface d'authenfication
def home(request):
    #cette fonction permet afficher le tableau de bord 
    
    nombre_client=adherant.objects.all().count()#cette variable consiste à stocker le nombre d'occurence entrer(le nombre d'adherant)
    nombre_voiture=vehicule.objects.all().count()#cette variable consiste à stocker le nombre d'occurence entrer(le nombre des vehicule)
    nombre_sinistre=sinistre.objects.all().count()#cette variable consiste à stocker le nombre d'occurence entrer(le nombre de sinistre)
    nombre_assurance=assure.objects.all().count()#cette variable consiste à stocker le nombre d'occurence entrer(le nombre d'assurance)
    context={'nombre_client':nombre_client,'nombre_voiture':nombre_voiture,'nombre_sinistre':nombre_sinistre,'nombre_assurance':nombre_assurance}
    return render(request,'dashbord/dashboard.html',context)

@login_required(login_url='compte:acces')
def list_adherant(request):#cette fonction consiste à afficher la liste d'adherant enregistrer 
    form=adherant.objects.all()
    context={'form':form}
    return render(request,'client/client.html',context)

@login_required(login_url='compte:acces')       
def enregistrerAdherant(request): #cette fonction consiste à enregistrer les nouveaux adherant 
    form=FormulaireAdherant()
    if request.method == 'POST':
       form=FormulaireAdherant(request.POST)
       if form.is_valid:
           form.save()
           context={'form':form}
           return render(request,'client/client-insert-update.html',context)
    context={'form':form}
    return render(request,'client/client-insert-update.html',context)

@login_required(login_url='compte:acces')
def enregistrerVoiture(request):#cette fonction consiste à enregistrer les nouvelles voitures
    form=FormulaireVoiture()
    if request.method == 'POST':
       form=FormulaireVoiture(request.POST)
       if form.is_valid:
           form.save()
    context={'form':form}
    return render(request,'vehicule/vehicule-insert-update.html',context)

@login_required(login_url='compte:acces')
def detail_adherant(request,pk):#cette fonction consiste à afficher les information sur une occurence(les informations sur l'adherants) grace à sa cle etrangere
    form=adherant.objects.get(id=pk)
    context={"form":form}
    return render(request,'client/client-details.html',context)

@login_required(login_url='compte:acces')
def modifier_detail_adherant(request,pk): #cette fonction consiste à modifier les information sur une occurence(les informations sur l'adherants) grace à sa cle etrangere
    ident=adherant.objects.get(id=pk)
    form=FormulaireAdherant(instance=ident)
    if request.method == 'POST':
        form=FormulaireAdherant(request.POST,instance=ident)
        if form.is_valid():
            form.save()
            form = adherant.objects.all()
            context = {'form': form}
            return render(request,'client/client.html',context)  
    context={'form':form}
    return render(request, 'client/client-insert-update.html', context)
    
@login_required(login_url='compte:acces')
def suprimer_adherant(request,pk):#cette fonction consiste à suprimer une occurence(l'adherants) grace à sa cle etrangere
     ident_adherant=adherant.objects.get(id=pk)
     ident_adherant.delete()
     form = adherant.objects.all()
     context = {'form': form}
     return render(request,'client/client.html',context)

@login_required(login_url='compte:acces')
def list_vehicule(request):#cette fonction consiste à afficher la liste des vehicules enregistrer 
    form=vehicule.objects.all() 
    context={'form':form}
    return render(request,'vehicule/vehicule.html',context)

@login_required(login_url='compte:acces')
def afficher_detail_voiture(request,pk):#cette fonction consiste à afficher la liste des vehicules enregistrer 
    form=vehicule.objects.get(id=pk)
    context={"form":form}
    return render(request,'vehicule/vehicule-details.html',context)

@login_required(login_url='compte:acces')
def  modifier_detail_vehicule(request,pk):#cette fonction consiste à afficher les information sur une occurence(les informations sur la voiture) grace à sa cle etrangere
     ident_vehicule=vehicule.objects.get(id=pk)
     form=FormulaireVoiture(instance=ident_vehicule)
     if request.method =='POST':
         form=FormulaireVoiture(request.POST,instance=ident_vehicule)
         if form.is_valid():
             form.save()
             form=vehicule.objects.all()
             context={'form':form}
             return render(request,'vehicule/vehicule.html',context)
    
     context={'form':form}
     return render(request, 'vehicule/vehicule-insert-update.html', context)

@login_required(login_url='compte:acces') 
def suprimer_vehicule(request,pk):
     ident_vehicule=vehicule.objects.get(id=pk)
     ident_vehicule.delete()
     form=vehicule.objects.all()
     context={'form':form}
     return  render(request,'vehicule/vehicule.html',context)
        
@login_required(login_url='compte:acces')
def list_sinistre(request):
    form=sinistre.objects.all()
    context={'form':form}
    return render(request,'sinistre/sinistre.html',context)

@login_required(login_url='compte:acces')
def enregistrerSinistre(request):
    form=FormulaireSinistre()
    if request.method == 'POST':
        form=FormulaireSinistre(request.POST)
        if form.is_valid:
            form.save()
            context={'form':form}
            return render(request,'sinistre/sinistre-insert-update.html',context)
    context={'form':form}
    return render(request,'sinistre/sinistre-insert-update.html',context)

@login_required(login_url='compte:acces')
def afficher_detail_sinistre(request,pk):
    ident_sinitre= sinistre.objects.get(id=pk)
    context={'form':ident_sinitre}
    return render(request,'sinistre/sinistre-details.html',context)

@login_required(login_url='compte:acces')
def modifier_detail_sinistre(request,pk):
    ident_sinistre=sinistre.objects.get(id=pk)
    form=FormulaireSinistre(instance=ident_sinistre)
    if request.method == 'POST':
        form=FormulaireSinistre(request.POST,instance=ident_sinistre)
        form.is_valid()
        form.save()
        form=sinistre.objects.all()
        context={'form':form}
        return render(request,'sinistre/sinistre.html',context)
    
    context={'form':form}
    return render(request,'sinistre/sinistre-insert-update.html',context)
   
@login_required(login_url='compte:acces')
def suprimer_sinistre(request,pk):
    form=sinistre.objects.get(id=pk)
    form.delete()
    form=sinistre.objects.all()
    context={'form':form}
    return render(request,'sinistre/sinistre.html',context)

@login_required(login_url='compte:acces')
def list_assurance(request):
    form=assure.objects.all()
    context={'form':form}
    return render(request,'assure/assurance.html',context)

@login_required(login_url='compte:acces')
def afficher_assurance(request,pk):
    form=assure.objects.get(id=pk)
    form_vehicule=vehicule.objects.get(id=pk)
    context={'form':form,'form_vehicule':form_vehicule}
    return render(request,'assure/assurance-details.html',context)

@login_required(login_url='compte:acces')
def enregistrement_assurance(request):
    form=FormulaireAssure()
    if request.method == 'POST':
         form=FormulaireAssure(request.POST)
         if form.is_valid():
            form.save()
            context={'form':form}
            return render(request,'assure/assurance-insert-update.html',context)
    context={'form':form}
    return render(request,'assure/assurance-insert-update.html',context)   
    
@login_required(login_url='compte:acces')
def modifier_detail_assurance(request,pk):
    ident_assurance=assure.objects.get(id=pk)
    form=FormulaireAssure(instance=ident_assurance)
    if request.method == 'POST':
        form=FormulaireAssure(request.POST,instance=ident_assurance)
        if form.is_valid():
            form.save()
            form=assure.objects.all()
            context={'form':form}
            return render(request,'assure/assurance.html',context)
    
    context={'form':form}
    return render(request,'assure/assurance-insert-update.html',context)

@login_required(login_url='compte:acces')
def suprimer_assurance(request,pk):
    form=assure.objects.get(id=pk)
    form.delete()
    form=assure.objects.all()
    context={'form':form}
    return render(request,'assure/assurance.html',context)


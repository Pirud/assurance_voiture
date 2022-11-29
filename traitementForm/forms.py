from django import forms
from django.forms import ModelForm
from adherant.models import adherant
from vehicule.models import vehicule
from sinistre.models import sinistre
from assure.models import assure
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class FormulaireAdherant(ModelForm):
    #cette classe permet de creer un formulaire d'enregistremment des adherants et d'ajouter le propriete bootstrap selon le template fournis
    matricule=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    nom=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    prenom=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    date_naissance=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control form-input"}))
    telephone=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    adresse=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control form-input","cols":30,"rows":5}))
    
    class Meta:
        model=adherant
        fields=('matricule','nom','prenom','date_naissance', 'telephone','adresse')

class FormulaireVoiture(ModelForm):
    #cette classe permet de creer un formulaire d'enregistremment de voiture et d'ajouter le propriete bootstrap selon le template fournis
    marque=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    model_v=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    immatriculation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    anne_mis_circulation=forms.DateField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    anne_de_fabrication=forms.DateField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    
    class Meta:
        model=vehicule
        fields=('proprietaire','marque','model_v','immatriculation', 'anne_mis_circulation','anne_de_fabrication','type_carburant')

class FormulaireSinistre(ModelForm):
    #cette classe permet de creer un formulaire d'enregistremment de sinistre et d'ajouter le propriete bootstrap venant selon le template fournis
    date_debut=forms.DateField(widget=forms.TextInput(attrs={'class':"form-control form-input"}))
    justification=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control form-input","cols":30,"rows":5}))
    class Meta:
        model=sinistre
        fields=('assure','adherant','date_debut','justification')
        
class FormulaireAssure(ModelForm):
    #cette classe permet de creer un formulaire et d'ajouter le propriete bootstrap venant selon le template fournis
    date_debut=forms.DateField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    date_ex=forms.DateField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    numero_assurance=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input"}))
    class Meta:
        model=assure
        fields=('type_ass','date_debut','fractionnement','date_ex', 'numero_assurance')
        


class CreerUtilisateur(UserCreationForm): 
#cette classe permet de generer le formulaire et d'ajouter le propriete bootstrap depuis le template qui genere le formulaire de creation de compte
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input","placeholder":"Votre nom d'utilisateur"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input","placeholder":"Votre adresse mail"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-input","placeholder":"Votre nouveau mot de passe"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-input","placeholder":"Confirmer votre mot de passe"}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
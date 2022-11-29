from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreerUtilisateur(UserCreationForm): 
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input","placeholder":"Votre nom d'utilisateur"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-input","placeholder":"Votre adresse mail"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-input","placeholder":"Votre nouveau mot de passe"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-input","placeholder":"Confirmer votre mot de passe"}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
        

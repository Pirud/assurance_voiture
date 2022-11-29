from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def formulaire_vehicule(request):
    return HttpResponse('liste des voiture')
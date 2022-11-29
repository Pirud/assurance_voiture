from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def affiche_sinitre(request):
    return HttpResponse('sinistre')
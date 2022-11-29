from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def affiche_assurance(request):
    return HttpResponse('application assurer')
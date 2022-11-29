from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def formulaire_client(request):
    return render(request,'formulaire_client.html')
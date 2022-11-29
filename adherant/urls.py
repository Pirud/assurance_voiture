from django.urls import path
from .import views

app_name='formulaire_adherant'
urlpatterns=[
    path('',views.formulaire_adherant,name='formulaire_adherant')
]
from django.urls import path
from .import views
app_name='vehicule'
urlpatterns=[
    path('',views.formulaire_vehicule,name='formulaire_vehicule')
]
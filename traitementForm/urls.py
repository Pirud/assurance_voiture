from django.urls import path
from .import views

app_name='traitementForm'
urlpatterns=[
    path('',views.home,name='home'),
    path('formulaire_adherant/',views.enregistrerAdherant,name='formulaire_adherant'),
     path('formulaire_voiture/',views.enregistrerVoiture,name='formulaire_voiture'),
     path('list_adherant/',views.list_adherant,name='list_adherant'),
    path('detail_adherant/<str:pk>',views.detail_adherant,name='detail_adherant'),
    path('modifier_detail_adherant/<str:pk>',views.modifier_detail_adherant,name='modifier_detail_adherant'),
    path('suprimer_adherant/<str:pk>',views.suprimer_adherant,name='suprimer_adherant'),
    path('list_vehicule/',views.list_vehicule,name='list_vehicule'),
    path('afficher_detail_voiture/<str:pk>',views.afficher_detail_voiture,name='afficher_detail_voiture'),
    path('modifier_detail_vehicule/<str:pk>',views.modifier_detail_vehicule,name='modifier_detail_vehicule'),
    path('suprimer_vehicule/<str:pk>',views.suprimer_vehicule,name='suprimer_vehicule'),
    path('list_sinistre/',views.list_sinistre,name='list_sinistre'),
    path('enregistrerSinistre/',views.enregistrerSinistre,name='enregistrerSinistre'),
    path('afficher_detail_sinistre/<str:pk>',views.afficher_detail_sinistre,name='afficher_detail_sinistre'),
    path('modifier_detail_sinistre/<str:pk>',views.modifier_detail_sinistre,name='modifier_detail_sinistre'),
    path('suprimer_sinistre/<str:pk>',views.suprimer_sinistre,name='suprimer_sinistre'),
    path('list_assurance/',views.list_assurance,name='list_assurance'),
    path('afficher_assurance/<str:pk>',views.afficher_assurance,name='afficher_assurance'),
    path('enregistrement_assurance/',views.enregistrement_assurance,name='enregistrement_assurance'),
    path('modifier_detail_assurance/<str:pk>',views.modifier_detail_assurance,name='modifier_detail_assurance'),
    path('suprimer_sinistre/<str:pk>',views.suprimer_sinistre,name='suprimer_sinistre'),
    
    
    
    
    
    
]
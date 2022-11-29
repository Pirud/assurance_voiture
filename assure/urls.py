from django.urls import path
from .import views

app_name='affiche_assurance'
urlpatterns=[
    path('',views.affiche_assurance,name='affiche_assurance')
]
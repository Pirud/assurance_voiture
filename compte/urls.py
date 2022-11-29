from django.urls import path
from .import views

app_name='compte'
urlpatterns=[
    path('inscription/',views.inscription,name='inscription'),
    path('acces/',views.acces,name='acces'),
    path('deconnecter/',views.deconnecter,name='deconnecter')
    ]
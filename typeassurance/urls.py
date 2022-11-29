from django.urls import path
from .import views

app_name='type_de_rassurance'
urlpatterns=[
    path('',views.type_de_assurance,name='type_de_rassurance')
]
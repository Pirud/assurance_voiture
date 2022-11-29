from django.db import models
from client.models import client
# Create your models here.
class adherant(client):

    matricule=models.CharField(max_length=200, null=True)
    
    
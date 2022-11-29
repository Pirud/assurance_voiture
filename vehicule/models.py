from django.db import models
from adherant.models import adherant
# Create your models here.

class vehicule(models.Model):

    proprietaire=models.ForeignKey(adherant, db_column='proprietaire_id' ,null=True, on_delete=models.SET_NULL)
    carburant=(('essence','essence'),('gazole','gazole'))
    marque=models.CharField(max_length=200, null=True)
    model_v=models.CharField(max_length=200, null=True)
    immatriculation=models.CharField(max_length=200, null=True)
    anne_mis_circulation=models.DateField()
    anne_de_fabrication=models.DateField()
    type_carburant=models.CharField(max_length=200,null=True,choices=carburant)
    date_enregistrement=models.DateTimeField(auto_now_add=True,null=True)
    

    
from django.db import models
from adherant.models import adherant
from assure.models import assure
# Create your models here.

class sinistre(models.Model):
    assure=models.ForeignKey(assure,null=True, on_delete=models.SET_NULL)
    adherant=models.ForeignKey(adherant,null=True,db_column='sinistré', on_delete=models.SET_NULL)
    date_debut=models.DateField()
    justification=models.CharField(max_length=500,null=True)
    date_justification=models.DateTimeField(auto_now_add=True,null=True)
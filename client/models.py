from django.db import models

# Create your models here.

class client(models.Model):
    nom=models.CharField(max_length=200, null=True)
    prenom=models.CharField(max_length=200, null=True)
    date_naissance=models.DateField()
    telephone=models.CharField(max_length=200,null=True)
    adresse=models.TextField(max_length=500, null=True)
    date_enregistrement=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        abstract=True
        
    def __str__(self) -> str:
        return self.nom
    
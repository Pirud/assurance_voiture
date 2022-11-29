from django.db import models
from typeassurance.models import typeassurance
# Create your models here.
class assure(models.Model):
    typ_fractionnement=(('mensuel','mensuel'),('annuel','annuel'))
    type_ass=models.ForeignKey(typeassurance,null=True, on_delete=models.SET_NULL)
    date_debut=models.DateField()
    fractionnement=models.CharField(max_length=200,null=True, choices=typ_fractionnement)
    date_ex=models.DateField()
    numero_assurance=models.CharField(max_length=200,null=True)
    
    def __str__(self) -> str:
        return str(self.type_ass)
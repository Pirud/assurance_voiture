from django.db import models

# Create your models here.
class typeassurance(models.Model):
    list_type_assurance=(('Automobile','Automobile'),('vie','vie'))
    type_ass=models.CharField(max_length=200, null=True, choices=list_type_assurance)
    
    def __str__(self) -> str:
        return self.type_ass
from django.contrib import admin
from .models import adherant
# Register your models here.

class adherantAdmin(admin.ModelAdmin):
    list_display=['matricule','nom','prenom','date_naissance', 'telephone','adresse','date_enregistrement']
    
    
admin.site.register(adherant,adherantAdmin)
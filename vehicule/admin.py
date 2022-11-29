from django.contrib import admin
from .models import vehicule
# Register your models here.

class VehiculeAdmin(admin.ModelAdmin):
    list_display=['proprietaire','marque','model_v','immatriculation', 'anne_mis_circulation','anne_de_fabrication','type_carburant','date_enregistrement']
admin.site.register(vehicule,VehiculeAdmin)
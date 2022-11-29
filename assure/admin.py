from django.contrib import admin
from assure.models import assure
# Register your models here.

class assureAdmin(admin.ModelAdmin):
    list_display=['type_ass','date_debut','fractionnement','date_ex', 'numero_assurance']
admin.site.register(assure,assureAdmin)
# Register your models here.

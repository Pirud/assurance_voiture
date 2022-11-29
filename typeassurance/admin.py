from django.contrib import admin
from typeassurance.models import typeassurance
# Register your models here.

class typeassuranceAdmin(admin.ModelAdmin):
    list_display=['type_ass']
admin.site.register(typeassurance,typeassuranceAdmin)
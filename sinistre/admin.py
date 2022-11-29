from django.contrib import admin
from .models import sinistre
# Register your models here.

class sinitreAdmin(admin.ModelAdmin):
    list_display=['assure','adherant','date_debut','justification', 'date_justification']
admin.site.register(sinistre,sinitreAdmin)
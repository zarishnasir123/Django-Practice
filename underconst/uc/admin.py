from django.contrib import admin
from .models import UnderConstruction

# Register your models here.
@admin.register(UnderConstruction)
class UnderConstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_under_construction', 'uc_duration', 'uc_note', 'updated_at')
    #tick box right in the list: one click + Save to switch the site on/off
    list_editable = ('is_under_construction',)

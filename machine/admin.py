from django.contrib import admin
from .models import Machine

# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'machine_type','machine_company')
    list_display_links = ('machine_name', 'machine_type','machine_company')
    list_filter = ('machine_type','machine_company')
    search_fields = ('machine_name',)
    list_per_page = 10


admin.site.register(Machine,MachineAdmin)
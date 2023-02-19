from django.contrib import admin
from .models import Offer

# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_display = ('customer', 'personel', 'machine','status','offer_date','note')
    list_display_links = ('customer', 'personel', 'machine','offer_date')
    list_filter = ('customer', 'personel', 'machine', 'status','offer_date')
    list_editable = ('status','note')
    search_fields = ('customer__company_name', 'personel__username', 'machine__machine_name', 'status','note')
    list_per_page = 10

admin.site.register(Offer,OfferAdmin)
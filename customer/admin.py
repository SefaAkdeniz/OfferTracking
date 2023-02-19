from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_phone','related_person_name1','related_person_phone1','related_person_mail1')
    list_display_links = ('company_name', 'company_phone','related_person_name1','related_person_phone1','related_person_mail1')
    list_filter = ('company_type','company_city','first_contact_date' )
    search_fields = ('company_name', 'company_phone','related_person_name1','related_person_phone1','related_person_mail1')
    list_per_page = 10

admin.site.register(Customer,CustomerAdmin)
from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'mobileNumber1', 'email')

admin.site.register(Contact, ContactAdmin)
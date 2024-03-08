from django.contrib import admin

from .models import *

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','question')
    fields=('name','email','question')
admin.site.register(ContactMessage,ContactMessageAdmin)
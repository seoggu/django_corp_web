from django.contrib import admin

from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
    readonly_fields = ('name','email','context')

# Register your models here.
admin.site.register(Inquiry, InquiryAdmin)
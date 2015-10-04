from django.contrib import admin
from .models import BusinessUser


# Register your models here.
class BusinessUserAdmin(admin.ModelAdmin):
	exclude = ['']

admin.site.register(BusinessUser, BusinessUserAdmin)

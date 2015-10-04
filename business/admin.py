from django.contrib import admin

from .models import Product, Material, Sale

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Sale)

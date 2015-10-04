from django.contrib import admin

from .models import Product, Material, Sale, Place

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Sale)
admin.site.register(Place)

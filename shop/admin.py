from django.contrib import admin
from shop.models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "stock", "oferta"]

admin.site.register(Producto, ProductoAdmin)

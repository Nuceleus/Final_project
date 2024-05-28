from django.contrib import admin
from .models import Producto, Servicio, DetalleVenta, Venta, Cliente


# Register your models here.

admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(DetalleVenta)
admin.site.register(Venta)
admin.site.register(Cliente)

from django.contrib import admin
from .models import reserva, pedido, producto

# Register your models here.

admin.site.register(producto)
admin.site.register(pedido)
admin.site.register(reserva)



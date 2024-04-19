from django.contrib import admin
from .models import usuario, tipo_usuario, reserva, pedido, producto

# Register your models here.

admin.site.register(usuario)
admin.site.register(tipo_usuario)
admin.site.register(reserva)
admin.site.register(pedido)
admin.site.register(producto)
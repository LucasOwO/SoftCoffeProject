from django.contrib import admin
from .models import usuario, tipo_usuario, reserva, pedido, producto, pedido_producto, pedido_usuario, usuario_reserva

# Register your models here.

admin.site.register(usuario)
admin.site.register(tipo_usuario)
admin.site.register(reserva)
admin.site.register(pedido)
admin.site.register(producto)
admin.site.register(pedido_usuario)
admin.site.register(pedido_producto)
admin.site.register(usuario_reserva)
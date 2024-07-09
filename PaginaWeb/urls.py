from django.urls import path
from . import views


#todas las urls van aquí
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('lobby', views.lobby),
    path('registro', views.registro),
    path('administrador/<cod_c>', views.administrador),
    path('agregar_producto', views.agregar_producto),
    path('eliminar_producto/<id_p>', views.eliminar_producto),
    path('editar_producto/<id_p>', views.editar_producto),
    path('editar_producto/editar_prod/<id_p>', views.editar_prod),
    path('Productos', views.mostrarProductos),
    path('carta', views.mostrarCarta),
    path('nosotros', views.acercaDeNostros),
    path('ofertas', views.mostrarOfertas),
    path('Pago', views.mostrarPago),
    path('reserva', views.reserva),
    
    
    
]
from django.urls import path
from . import views

#todas las urls van aquí
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('lobby', views.lobby),
    path('registro', views.registro),
    path('administrador', views.administrador),
    path('agregar_producto', views.agregar_producto),
    path('eliminar_producto/<id_prod>', views.eliminar_producto),
    path('editar_producto', views.editar_producto),
    path('Productos', views.mostrarProductos),
    path('carta', views.mostrarCarta),
    path('nosotros', views.acercaDeNostros),
    path('ofertas', views.mostrarOfertas)
]
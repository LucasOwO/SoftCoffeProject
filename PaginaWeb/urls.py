from django.urls import path
from . import views

#todas las urls van aquí
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('lobby', views.lobby),
    path('registro', views.registro),
    path('administrador', views.administrador),
    path('listaProductos', views.listaProductos)
    path('Productos', views.mostrarProductos),
    path('carta', views.mostrarCarta),
    path('nosotros', views.acercaDeNostros),
    path('ofertas', views.mostrarOfertas)
]
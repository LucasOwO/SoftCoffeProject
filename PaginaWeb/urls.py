from django.urls import path
from . import views

#todas las urls van aquí
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('lobby', views.lobby),
    path('registro', views.registro),
    path('Productos', views.mostrarProductos),
    path('carta', views.mostrarCarta),
    path('acercadenosotros', views.acercaDeNostros),
    path('ofertas', views.mostrarOfertas)

]
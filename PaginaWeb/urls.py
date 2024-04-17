from django.urls import path
from . import views

#todas las urls van aquí
urlpatterns = [
    path('', views.mostrarMain),
    path('login', views.mostrarLogin),
    path('lobby', views.mostrarLobby)
]
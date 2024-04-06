from django.urls import path
from . import views

#todas las urls van aquí
urlpatterns = [
    path('', views.mostrarpag)
]
"""SoftCoffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PaginaWeb.views import PayView, CrearOrden

urlpatterns = [
    path('', include('PaginaWeb.urls')),
    path('login/', include('PaginaWeb.urls')),
    path('registro/', include('PaginaWeb.urls')),
    path('lobby/', include('PaginaWeb.urls')),
    path('administrador/', include('PaginaWeb.urls')),
    path('agregar_producto/', include('PaginaWeb.urls')),
    path('eliminar_producto/', include('PaginaWeb.urls')),
    path('editar_producto/', include('PaginaWeb.urls')),
    path('editar_producto/', include('PaginaWeb.urls')),
    path('admin/', admin.site.urls),
    path('Productos/', include('PaginaWeb.urls')),
     path('reserva/', include('PaginaWeb.urls')),
    path('carta/', include('PaginaWeb.urls')),
    path('ofertas/', include('PaginaWeb.urls')),
    path('nosotros/', include('PaginaWeb.urls')),
    path('Pago/', include('PaginaWeb.urls')),
    path('pay/', PayView.as_view(), name ='pay-paypal'),
    path('api/orders', CrearOrden.as_view())
    
    
]

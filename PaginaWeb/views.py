from django.shortcuts import render
from .models import producto


# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def lobby(request):
    context = {}
    return render(request, 'lobby.html', context)

def registro(request):
    context = {}
    return render(request, 'registro.html', context)

def administrador(request):
    lista_productos = producto.objects.all()
    return render(request, 'administrador.html', {"productos": lista_productos})

def listaProductos(request):
    lista_productos = producto.objects.all()
    return render(request, 'iframes/listaProductos.html', {"productos": lista_productos})
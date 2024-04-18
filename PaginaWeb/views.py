from django.shortcuts import render


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
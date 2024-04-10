from django.shortcuts import render


# Create your views here.

def mostrarMain(request):
    context = {}
    return render(request, 'Main/Main.html', context)


def mostrarLogin(request):
    context = {}
    return render(request, 'Login/login.html', context)
from django.shortcuts import render


# Create your views here.

def mostrarpag(request):
    context = {}
    return render(request, 'Main/Main.html', context)
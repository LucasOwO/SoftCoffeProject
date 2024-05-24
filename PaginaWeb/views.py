from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import producto
from django.views import View
from django.views.generic import FormView, TemplateView
from .funciones import generateAccessToken


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
  
def mostrarProductos(request):
    lista_p = producto.objects.filter(categoria="Cafe")
    return render(request, 'Productos.html', {"productos": lista_p})

def mostrarOfertas(request):
    context = {}
    return render(request, 'ofertas.html', context)

def acercaDeNostros(request):
    context = {}
    return render(request, 'nosotros.html', context)

def mostrarCarta(request):
    context = {}
    return render(request, 'carta.html', context)

def mostrarPago(request):
    context ={}
    return render(request, 'Pago.html', context)

def agregar_producto(request):
    nom_p = request.POST['txt_nombre']
    precio_p = request.POST['txt_precio']
    categ_p = request.POST['txt_categ']
    stock_p = request.POST['txt_stock']
    desc_p = request.POST['txt_desc']
    img_p = request.POST['archivo_img']

    list_p = producto.objects.all()
    id_p = len(list_p)+1

    nuevo_producto = producto.objects.create(id_prod=id_p, nombre=nom_p, precio=precio_p, categoria=categ_p,stock=stock_p, descripcion=desc_p, imagen=img_p)
    return redirect('/administrador')
    
def eliminar_producto(request,id_prod):
    prod = producto.objects.get(id_prod=id_prod)
    prod.delete()

    return redirect('/administrador')

def editar_producto():
    return redirect('/administrador')

#CONFIGURACION DE PAYPAL

class PayForm(forms.Form):
    count = forms.IntegerField()
    
    
class PayView(FormView):
    tamplate_name = 'pago.html'
    form_class = PayForm
    success_url = '/'
    
def form_valid(self, form):
    print(form.cleaned_data['count'])
    #
    print("------------")
    respuesta = generateAccessToken()
    print(respuesta)
    return super.form_valid(form)


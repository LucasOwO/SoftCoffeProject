from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import producto, categoria
from django.views import View
from django.views.generic import FormView, TemplateView
from .funciones import create_order, generateAccessToken
#
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Renderización de páginas

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
    lista_productos = producto.objects.all().order_by("-id_prod")
    lista_categorias = categoria.objects.all()
    return render(request, 'administrador.html', {"productos": lista_productos,"categorias": lista_categorias})

def editar_producto(request,id_p):
    prod = producto.objects.get(id_prod = str(id_p))
    lista_categorias = categoria.objects.all()
    return render(request, 'editar_producto.html', {"producto": prod,"categorias": lista_categorias})
  
def mostrarProductos(request):
    lista_p = producto.objects.filter(categoria=1)
    return render(request, 'Productos.html', {"productos": lista_p})

def reserva(request):
    context={}
    return render(request, 'reserva.html', context)

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





# Funcionalidades

def agregar_producto(request):
    nom_p = request.POST['txt_nombre']
    precio_p = request.POST['txt_precio']
    categ_p = categoria.objects.get(cod_categ = request.POST['categ'])
    stock_p = request.POST['txt_stock']
    desc_p = request.POST['txt_desc']
    #img_p = request.POST['archivo_img']

    list_p = producto.objects.all().order_by('-id_prod')
    try:
        n = list_p[0].id_prod
        id_p = n+1
    except:
        id_p = 1

    nuevo_producto = producto.objects.create(id_prod=id_p, nombre=nom_p, precio=precio_p, categoria=categ_p,stock=stock_p, descripcion=desc_p)
    return redirect('/administrador')
    
def eliminar_producto(request,id_p):
    prod = producto.objects.get(id_prod=id_p)
    prod.delete()
    return redirect('/administrador')

def editar_prod(request, id_p):
    prod = producto.objects.get(id_prod=id_p)
    
    prod.nombre = request.POST['txt_nombre']
    prod.precio = request.POST['txt_precio']
    prod.stock = request.POST['txt_stock']
    prod.descripcion = request.POST['txt_desc']
    
    if request.POST['categ'] != "NULO":
        prod.categoria =  categoria.objects.get(cod_categ = request.POST['categ'])
    
    prod.save()
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

class CrearOrden(APIView):
    
    def post(self, request):

        order = create_order('Productos')
        print('-------------')
        #print(order['id'])
        return Response({'code': 'ok'}, status = status.HTTP_200_OK )


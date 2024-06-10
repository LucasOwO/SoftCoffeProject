from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from PaginaWeb.funciones import capture_order, create_order, generateAccessToken
from .models import producto
from django.views import View
from django.views.generic import FormView, TemplateView

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
    return render(request, 'administrador.html', {"productos": lista_productos})
  
def mostrarProductos(request):
    lista_p = producto.objects.filter(categoria="Cafe")
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

#PAYPAL

class PayForm(forms.Form):
    count = forms.IntegerField()
    
class PayView(FormView):
    template_name = 'pay.html'
    form_class = PayForm
    success_url = '/'
    
    def form_valid(self, form):
        print(form.cleaned_data['count'])
        #
        print('----')
        respuesta = generateAccessToken()
        print(respuesta)
        return super().form_valid(form)


class CrearOrden(APIView):
    
    def post(self, request):
        order = create_order('Productos')
        print('=====')
        print(order['id'])
        return Response(order, status=status.HTTP_200_OK)


class CapturarOdernPaypal(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            order_id = self.kwargs['order_id']
            response = capture_order(order_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'error': 'error aqui'}, status=status.HTTP_400_BAD_REQUEST)   




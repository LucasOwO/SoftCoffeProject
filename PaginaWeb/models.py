from django.db import models

# Create your models here.

class usuario(models.Model):
    id_usuario = models.PositiveIntegerField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    fec_nac = models.DateField()
    correo = models.CharField(max_length=40)
    contra = models.CharField(max_length=40)
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombres, self.apellidos)

class tipo_usuario(models.Model):
    id_tipo = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
    
class reserva(models.Model):
    id_reserva = models.PositiveIntegerField(primary_key=True)
    fec_res = models.DateField();
    
    def __str__(self):
        texto = "Reserva nro {0}"
        return texto.format(self.id_reserva)
    
class pedido(models.Model):
    cod_pedido = models.PositiveIntegerField(primary_key=True)
    fec_ped = models.DateField()
    
    def __str__(self):
        texto = "Pedido {0}"
        return texto.format(self.cod_pedido)

class producto(models.Model):
    id_prod = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=300)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
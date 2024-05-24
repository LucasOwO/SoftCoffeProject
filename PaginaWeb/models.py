from django.db import models

# Create your models here.

class tipo_usuario(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)

class usuario(models.Model):
    id_usuario = models.PositiveIntegerField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    fec_nac = models.DateField()
    correo = models.CharField(max_length=40)
    contra = models.CharField(max_length=40)
    tipo_usuario = models.ForeignKey(tipo_usuario, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombres, self.apellidos)
    
class producto(models.Model):
    id_prod = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio = models.PositiveIntegerField()
    categoria = models.CharField(max_length=25, null=True)
    stock = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to = 'IMGS/% Y/% m/% d/', null=True)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
    
class pedido(models.Model):
    cod_pedido = models.PositiveIntegerField(primary_key=True)
    fec_ped = models.DateField()
    
    def __str__(self):
        texto = "Pedido {0}"
        return texto.format(self.cod_pedido)

class medio_pago(models.Model):
    id_pago = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    

class pedido_producto(models.Model):
    cod_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class pedido_usuario(models.Model):
    cod_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_pago = models.ForeignKey(medio_pago, on_delete=models.CASCADE)
    

class reserva(models.Model):
    id_reserva = models.PositiveIntegerField(primary_key=True)
    fec_res = models.DateField()
    
    def __str__(self):
        texto = "Reserva nro {0}"
        return texto.format(self.id_reserva)
   
class usuario_reserva(models.Model):
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(reserva, on_delete=models.CASCADE)

from django.db import models
# Create your models here.

class categoria(models.Model):
    id_categ = models.PositiveIntegerField(primary_key=True)
    cod_categ = models.CharField(max_length=5)
    nom_categ = models.CharField(max_length=30)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nom_categ)

class producto(models.Model):
    id_prod = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=300)
    #imagen = models.ImageField(upload_to = 'IMGS / %Y/ %m /%d/', null=True)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
    
class pedido(models.Model):
    cod_pedido = models.PositiveIntegerField(primary_key=True)
    fec_ped = models.DateField()
    
    def __str__(self):
        texto = "Pedido {0}"
        return texto.format(self.cod_pedido)
    
class producto_pedido(models.Model):
    cod_pedido_FK = models.ForeignKey(pedido, on_delete=models.CASCADE)
    id_prod_FK = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class reserva(models.Model):
    id_reserva = models.PositiveIntegerField(primary_key=True)
    fec_res = models.DateField()
    
    def __str__(self):
        texto = "Reserva nro {0}"
        return texto.format(self.id_reserva)
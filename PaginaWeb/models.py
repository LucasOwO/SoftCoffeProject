from django.db import models

categorias_choices = (
    ("CF","Cafés"),
    ("SW", "Sandwiches"),
    ("TG", "Tragos"),
    ("PCT", "Picoteos"),
    ("TT", "Tortas"),
    ("PTR", "Postres"),
    ("EX", "Extras"),
    ("OTR", "Otros"),
)


# Create your models here.

class producto(models.Model):
    id_prod = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio = models.PositiveIntegerField()
    categoria = models.CharField(max_length=15, choices=categorias_choices, default='OTR')
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

class reserva(models.Model):
    id_reserva = models.PositiveIntegerField(primary_key=True)
    fec_res = models.DateField()
    
    def __str__(self):
        texto = "Reserva nro {0}"
        return texto.format(self.id_reserva)
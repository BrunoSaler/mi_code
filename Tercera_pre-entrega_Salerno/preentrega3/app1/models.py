from django.db import models

category=[
    ("1", 'Línea Blanca'),
    ("2", 'Electrodoméstico'),
    ("3", 'Informática'),
    ("4", 'Pendiente')
]

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nacimiento = models.DateField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class producto(models.Model):
    producto = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=category, default=4)
    #cant_disponible = models.IntegerField()
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.modelo

class compras(models.Model):
    usuario = models.ForeignKey(usuario, null=True, on_delete=models.SET_NULL)
    fecha_compra = models.DateField()
    producto = models.ForeignKey(producto, on_delete=models.PROTECT)










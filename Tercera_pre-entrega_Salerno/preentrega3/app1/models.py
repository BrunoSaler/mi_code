from django.db import models

category=(
    (1, 'Línea Blanca'),
    (2, 'Electrodoméstico'),
    (3, 'Informática'),
)

prov=(
    (1, 'Buenos Aires'),
    (2, 'C.A.B.A.'),
    (3, 'Catamarca'),
    (4, 'Chaco'),
    (5, 'Chubut'),
    (6, 'Córdoba'),
    (7, 'Corrientes'),
    (8, 'Entre Ríos'),
    (9, 'Formosa'),
    (10, 'Jujuy'),
    (11, 'La Pampa'),
    (12, 'La Rioja'),
    (13, 'Mendoza'),
    (14, 'Misiones'),
    (15, 'Neuquén'),
    (16, 'Río Negro'),
    (17, 'Salta'),
    (18, 'San Juan'),
    (19, 'San Luis'),
    (20, 'Santa Cruz'),
    (21, 'Santa Fe'),
    (22, 'Santiago del Estero'),
    (23, 'Tierra del Fuego'),
    (24, 'Tucumán'),
    (25, 'Islas Malvinas'),
)

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    nacimiento = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.email

class Producto(models.Model):
    producto = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=category)
    #cant_disponible = models.IntegerField()
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.modelo

class Compras(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    fecha_compra = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    dir_envio = models.CharField(max_length=1000)
    provincia_envio = models.IntegerField(choices=prov)










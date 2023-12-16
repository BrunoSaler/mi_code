from django.db import models
from django.contrib.auth.forms import UserModel
from django.contrib.auth.models import User

category=(
    (1, 'Línea Blanca'),
    (2, 'Electro'),
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

class UpperField(models.CharField): #INTERVENGO CHARFIELD PARA QUE ME LO TOME EN MAYÚSCULA
    def get_prep_value(self, value):
        return str(value).upper()

class Producto(models.Model):
    modelo = UpperField(max_length=100, unique=True)
    producto = UpperField(max_length=100)
    categoria = models.IntegerField(choices=category)
    marca = UpperField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.modelo
    
class InfoProd(models.Model):
    modelo = models.OneToOneField(Producto, on_delete=models.CASCADE) #CUANDO BORRO EL PRODUCTO, QUE BORRE LA RESEÑA
    titulo = models.CharField(max_length=100, blank=False, null=False)
    cuerpo = models.TextField()
    imagen = models.FileField(upload_to="productos")

    def __str__(self):
        return f"Info {self.modelo}"
    
class Compras(models.Model):
    usuario = models.ForeignKey(UserModel, null=True, on_delete=models.SET_NULL)
    fecha_compra = models.DateField()
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    dir_envio = UpperField(max_length=1000)
    provincia_envio = models.IntegerField(choices=prov)

    def __str__(self):
        return f"Compra {self.usuario} {self.producto}"
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Avatar {self.user}"
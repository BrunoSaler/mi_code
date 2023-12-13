from django.db import models

category=(
    (1, 'Línea Blanca'),
    (2, 'Electro'),
    (3, 'Informática'),
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
        return f"{self.modelo} {self.imagen}"
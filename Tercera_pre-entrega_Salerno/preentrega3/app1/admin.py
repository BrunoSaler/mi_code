from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.usuario)
admin.site.register(models.producto)
admin.site.register(models.compras)
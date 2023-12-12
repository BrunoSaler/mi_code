from django.shortcuts import get_object_or_404, render, redirect
#from django.contrib import messages
#from django.contrib.messages import get_messages
from datetime import date
from . import models

def date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]                                  
    year = date.year
    return f"{day} de {month} de {year}"

def view_home(request):
    nombre = "Bruno"
    apellido = "Salerno"
    fecha = date_format(date.today())
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        'fecha': fecha,
    }  # Para enviar al contexto
    return render(request, "base/home.html", diccionario)

def view_about(request):
    return render(request, "base/about.html")

def view_list_lb(request):
    producto_filtrado = []
    for producto in models.Producto.objects.filter(categoria="1"):
        producto_filtrado.append(producto)
    return render(request, "base/verproductos.html", {"productos": producto_filtrado})

def view_list_electro(request):
    producto_filtrado = []
    for producto in models.Producto.objects.filter(categoria="2"):
        producto_filtrado.append(producto)
    return render(request, "base/verproductos.html", {"productos": producto_filtrado})

def view_list_info(request):
    producto_filtrado = []
    for producto in models.Producto.objects.filter(categoria="3"):
        producto_filtrado.append(producto)
    return render(request, "base/verproductos.html", {"productos": producto_filtrado})
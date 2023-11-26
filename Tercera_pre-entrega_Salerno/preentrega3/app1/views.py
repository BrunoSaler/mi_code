from django.shortcuts import render
from datetime import date

def date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]                                  
    year = date.year
    return f"{day} de {month} de {year}"

def view_bienvenida(request):
    nombre = "Bruno"
    apellido = "Salerno"
    fecha = date_format(date.today())
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        'fecha': fecha,
    }  # Para enviar al contexto
    return render(request, "app1/welcome.html", diccionario)
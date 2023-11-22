from django.shortcuts import render
from datetime import date

def view_bienvenida(request):
    return render(request, "act3/welcome.html")#aca el template es estático

def view_autor(request):
    nombre = "Bruno"
    apellido = "Salerno"
    fecha = date.today()
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        'fecha': fecha,
    }  # Para enviar al contexto
    return render(request, "act3/autor.html", diccionario)#aca le paso datos al template

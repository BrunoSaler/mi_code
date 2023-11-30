from time import sleep
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from . import forms, models


def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

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

def view_registrar_usuario(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Te has registrado correctamente.")
            return redirect("/registro")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/registro")
    else:
        form = forms.UsuarioForm()
    return render(request, "app1/registrousuario.html", {"form": form})

def view_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = models.Usuario.objects.filter(email__contains=email, password__contains=password)
            if user:
                messages.success(request, "Login exitoso.")
                return redirect("/login")
            else:
                messages.error(request, "Usuario no registrado.")
                return redirect("/login")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/login")
    else:
        form = forms.LoginForm()
    return render(request, "app1/login.html", {"form": form})
    
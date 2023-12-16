from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from . import forms

def view_register(request):

    if request.method == "GET":
        return render(
            request,"autentifications/registro.html",{"form": forms.RegistroForm()})
    else:
        form = forms.RegistroForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data["username"]
            form.save()
            return render(request,"autentifications/registrok.html", {"usuario": usuario})
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return render(request,"autentifications/registro.html",{"form": form})

def view_login(request):
    if request.user.is_authenticated:
        messages.error(request, f"{usuario} ya esta logueado.")
        return render(request,"base/home.html")
    if request.method == "GET":
        return render(
            request,"autentifications/login.html",{"form": AuthenticationForm()})
    else:
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data["username"]
            password = data["password"]
            persona= authenticate(username=usuario, password=password)
            login(request, persona)
            return render(request,"autentifications/loginexitoso.html")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return render(request,"autentifications/login.html",{"form": formulario})
        
def view_logout(request):
    logout(request)
    return render(request,"autentifications/logout.html")

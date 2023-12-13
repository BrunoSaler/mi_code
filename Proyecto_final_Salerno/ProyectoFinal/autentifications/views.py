from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
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
            messages.error(request, f"{usuario} fue registrado correctamente.")
            return render(request,"base/home.html")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return render(request,"autentifications/registro.html",{"form": form})

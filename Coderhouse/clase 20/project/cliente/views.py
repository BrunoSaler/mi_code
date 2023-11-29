from datetime import date

from django.shortcuts import redirect, render

# from .models import Cliente, Pais
from . import models


def home(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)


def crear_clientes_varios(request):
    p1 = models.Pais(nombre="Paraguay")
    p2 = models.Pais(nombre="México")
    p3 = models.Pais(nombre="El Salvador")
    p1.save()
    p2.save()
    p3.save()
    c1 = models.Cliente(nombre="Almendra", apellido="Ruiseñor", nacimiento=date(2015, 1, 1), pais_origen=p1)
    c2 = models.Cliente(nombre="Giordana", apellido="Tapello", nacimiento=date(2005, 2, 2), pais_origen=p2)
    c3 = models.Cliente(nombre="Macarena", apellido="Lito", nacimiento=date(1990, 1, 1), pais_origen=p3)
    c4 = models.Cliente(nombre="Jhiordana", apellido="Perez", nacimiento=date(2005, 1, 1), pais_origen=None)
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:index")


def busqueda(request):
    # búsqueda por nombre que contenga "dana"
    cliente_nombre = models.Cliente.objects.filter(nombre__contains="dana")

    # nacimientos mayores a 2000
    cliente_nacimiento = models.Cliente.objects.filter(nacimiento__gt=date(2000, 1, 1))

    # país de origen vacío (null - None)
    cliente_pais = models.Cliente.objects.filter(pais_origen=None)

    context = {
        "cliente_nombre": cliente_nombre,
        "cliente_nacimiento": cliente_nacimiento,
        "cliente_pais": cliente_pais,
    }
    return render(request, "cliente/busqueda.html", context)


from . import forms


def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

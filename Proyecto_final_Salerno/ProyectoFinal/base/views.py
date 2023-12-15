from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from . import models, forms
from django.contrib.auth.models import User

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

def view_infoprod(request, modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    info = []
    for x in models.InfoProd.objects.filter(modelo=id):
        info.append(x)
    return render(request, "base/infoprod.html", {"descripcion": info})

@login_required
def view_menu(request):
    if (request.user.is_superuser):
        return render(request, "base/adminmenu.html")
    else:
        return render(request, "base/usermenu.html")
    
class CrearProductoView(LoginRequiredMixin, CreateView):
    model = models.Producto
    template_name = "base/crear_producto.html"
    success_url = reverse_lazy("productlist")
    fields = "__all__"

class ProductoView(LoginRequiredMixin, ListView):
    model = models.Producto
    context_object_name = "productos"
    template_name = "base/lista_productos.html"

class ModificarProductoView(LoginRequiredMixin, UpdateView):
    model = models.Producto
    template_name = "base/update_producto.html"
    success_url = reverse_lazy("productlist")
    fields = ["producto", "categoria", "marca", "precio"]

class BorrarProductoView(LoginRequiredMixin, DeleteView):
    model = models.Producto
    template_name = "base/borrar_producto.html"
    success_url = reverse_lazy("productlist")

class CrearInfoView(LoginRequiredMixin, CreateView):
    model = models.InfoProd
    template_name = "base/crear_info.html"
    success_url = reverse_lazy("productlist")
    fields = "__all__"

@login_required
def view_infoprod_admin(request, modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    info = []
    for x in models.InfoProd.objects.filter(modelo=id):
        info.append(x)
    return render(request, "base/infoprod_admin.html", {"descripcion": info})

@login_required
def view_infoprod_edit(request,modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    info = get_object_or_404(models.InfoProd,modelo=id)
    if request.method == 'POST':
        form = forms.EditInfoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            info.titulo = data["titulo"]
            info.cuerpo = data["cuerpo"]
            info.imagen = data["imagen"]
            info.save()
            return redirect("productlist")        
        return render(request, "base/update_info.html", {"form":form})  
    else:
        form = forms.EditInfoForm()
        return render(request, "base/update_info.html", {"form":form})

@login_required
def view_infodelete(request, modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    
    if request.method == 'POST':
        info = get_object_or_404(models.InfoProd,modelo=id)
        info.delete()
        #profesores = Profesor.objects.all()
        return redirect("productlist")  
    return render(request, "base/borrar_info.html")

@login_required
def view_ingresar_compra(request):
    if request.method == "POST":
        form = forms.ComprasForm(request.POST)
        if form.is_valid():
            fecha_compra = form.cleaned_data['fecha_compra']
            producto = form.cleaned_data['producto']
            dir_envio = form.cleaned_data['dir_envio']
            provincia_envio = form.cleaned_data['provincia_envio']
            user = User.objects.get(id=request.user.id)
            modelo = models.Compras(fecha_compra = fecha_compra, producto= producto, dir_envio=dir_envio, provincia_envio=provincia_envio, usuario=user )
            modelo.save()
            messages.success(request, "Compra ingresada.")
            return redirect("/menu")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu")
    else:
        form = forms.ComprasForm()
    return render(request, "base/ingresocompras.html", {"form": form})

@login_required
def view_ver_compras(request):
    compras = []
    user = User.objects.get(id=request.user.id)
    for i in models.Compras.objects.filter(usuario=user):
        compras.append(i)
    return render(request, "base/vercompras.html", {"compras": compras})

@login_required
def view_ver_compras_admin(request):
    compras = []
    for i in models.Compras.objects.all():
        compras.append(i)
    return render(request, "base/vercomprasadmin.html", {"compras": compras})
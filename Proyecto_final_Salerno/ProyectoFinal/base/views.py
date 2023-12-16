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
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    nombre = "Bruno"
    apellido = "Salerno"
    fecha = date_format(date.today())
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        'fecha': fecha,
        'avatar_url': avatar_url
    }  # Para enviar al contexto
    return render(request, "base/home.html", diccionario)

def view_about(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
    }
    return render(request, "base/about.html", diccionario)

def view_list_lb(request):
    producto_filtrado = []
    for producto in models.Producto.objects.filter(categoria="1"):
        producto_filtrado.append(producto)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "productos": producto_filtrado,
    }
    return render(request, "base/verproductos.html", diccionario)

def view_list_electro(request):
    producto_filtrado = []
    for producto in models.Producto.objects.filter(categoria="2"):
        producto_filtrado.append(producto)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "productos": producto_filtrado,
    }
    return render(request, "base/verproductos.html", diccionario)

def view_list_info(request):
    producto_filtrado = []
    for producto in models.Producto.objects.filter(categoria="3"):
        producto_filtrado.append(producto)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "productos": producto_filtrado,
    }
    return render(request, "base/verproductos.html", diccionario)

def view_infoprod(request, modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    info = []
    for x in models.InfoProd.objects.filter(modelo=id):
        info.append(x)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "descripcion": info,
    }
    return render(request, "base/infoprod.html", diccionario)

@login_required
def view_menu(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
    }
    if (request.user.is_superuser):
        return render(request, "base/adminmenu.html", diccionario)
    else:
        return render(request, "base/usermenu.html", diccionario)

@login_required    
def CrearProductoView(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto ingresado.")
            return redirect("productlist")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/newproduct")
    else:
        form = forms.ProductoForm()
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "form": form,
        }
    return render(request, "base/crear_producto.html", diccionario)

@login_required
def ProductoView(request):
    productos = []
    for i in models.Producto.objects.all():
        productos.append(i)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "productos": productos,
        }
    return render(request, "base/lista_productos.html", diccionario)

@login_required
def ModificarProductoView(request, id):
    product = models.Producto.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProductoEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product.modelo = product.modelo
            product.producto = data["producto"]
            product.categoria = data["categoria"]
            product.marca = data["marca"]
            product.precio = data["precio"]  
            product.save()
            messages.success(request, "Producto modificado.")
            return redirect("productlist")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("productlist")
    else:
        form = forms.ProductoEditForm(initial={"producto": product.producto,"categoria": product.categoria,"marca": product.marca,"precio": product.precio})
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "form": form,
            "id": product.id
            }
        return render(request, "base/update_producto.html", diccionario)

@login_required
def BorrarProductoView(request, id):
    if request.method == 'POST':
        product = models.Producto.objects.get(id=id)
        product.delete()
        messages.success(request, "Producto eliminado.")
        return redirect("productlist")
    else:
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            }
        return render(request, "base/borrar_producto.html", diccionario)

@login_required
def CrearInfoView(request):
    if request.method == "POST":
        form = forms.InfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Reseña ingresada.")
            return redirect("productlist")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("productlist")
    else:
        form = forms.InfoForm()
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "form": form,
        }
    return render(request, "base/crear_info.html", diccionario)


"""class CrearInfoView(LoginRequiredMixin, CreateView):
    model = models.InfoProd
    template_name = "base/crear_info.html"
    success_url = reverse_lazy("productlist")
    fields = "__all__" """

@login_required
def view_infoprod_admin(request, modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    info = []
    for x in models.InfoProd.objects.filter(modelo=id):
        info.append(x)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "descripcion": info,
    }
    return render(request, "base/infoprod_admin.html", diccionario)

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
            messages.success(request, "Reseña modificada.")
            return redirect("productlist")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("productlist")
    else:
        form = forms.EditInfoForm()
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "form":form,
        }
        return render(request, "base/update_info.html", diccionario)

@login_required
def view_infodelete(request, modelo):
    modelo=modelo[1:-1]
    aux = get_object_or_404(models.Producto,modelo=modelo)
    id = aux.pk
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
    }
    if request.method == 'POST':
        info = get_object_or_404(models.InfoProd,modelo=id)
        try:
            info.delete()
            messages.success(request, "Reseña eliminada.")
            return redirect("productlist")
        except:   
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("productlist")
    return render(request, "base/borrar_info.html", diccionario)

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
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "form": form,
        }
    return render(request, "base/ingresocompras.html", diccionario)

@login_required
def view_ver_compras(request):
    compras = []
    user = User.objects.get(id=request.user.id)
    for i in models.Compras.objects.filter(usuario=user):
        compras.append(i)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "compras": compras,
    }
    return render(request, "base/vercompras.html", diccionario)

@login_required
def view_ver_compras_admin(request):
    compras = []
    for i in models.Compras.objects.all():
        compras.append(i)
    return render(request, "base/vercomprasadmin.html", {"compras": compras})

@login_required
def view_perfil(request):
    usuario = request.user
    avatar = models.Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    diccionario = {
        'avatar_url': avatar_url,
        "user": usuario,
    }
    return render(request, "base/veruser.html", diccionario)


@login_required
def view_editar_perfil(request):
    usuario = request.user
    if request.method == "GET":
        valores_iniciales = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name}
        form = forms.UserEditForm(initial=valores_iniciales)
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "usuario": usuario,
            "form": form,
        }
        return render(request,"base/editar_perfil.html", diccionario)
    else:
        form = forms.UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("/")

@login_required
def view_avatar(request):
    usuario = request.user
    if request.method == "GET":
        form = forms.UserAvatarForm()
        if request.user.is_authenticated:
            usuario = request.user
            avatar = models.Avatar.objects.filter(user=usuario).last()
            avatar_url = avatar.imagen.url if avatar is not None else ""
        else:
            avatar_url = ""
        diccionario = {
            'avatar_url': avatar_url,
            "usuario": usuario,
            "form": form,
        }
        return render(request,"base/edit_avatar.html", diccionario)
    else:
        formulario = forms.UserAvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            modelo = models.Avatar(user=usuario, imagen=data["imagen"])
            modelo.save()
            return redirect("/menu/view_profile")
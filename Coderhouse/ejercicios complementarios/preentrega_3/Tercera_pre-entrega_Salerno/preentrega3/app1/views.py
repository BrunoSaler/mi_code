from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from datetime import date
from . import forms, models

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
    return render(request, "registration/registrousuario.html", {"form": form})

def view_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = models.Usuario.objects.get(email__exact=email)
                if ((user is not None) and (user.password==password)):
                    if (user.email=="manager@electrolaucha.com"):
                        return redirect("/managermenu")
                    else:
                        #messages.success(request, f"{user.nombre}")
                        return redirect("/usermenu")
                else:
                    messages.error(request, "Contraseña errónea.")
                    return redirect("/login")
            except:
                messages.error(request, "Usuario no registrado.")
                return redirect("/login")                
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/login")
    else:
        form = forms.LoginForm()
    return render(request, "registration/login.html", {"form": form})

def view_managermenu(request):
    return render(request, "users/managermenu.html")

def view_usermenu(request):
    return render(request, "users/usermenu.html")

def view_ingresar_producto(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto ingresado.")
            return redirect("/managermenu")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/managermenu/ingresoproducto")
    else:
        form = forms.ProductoForm()
    return render(request, "users/ingresoproducto.html", {"form": form})

def view_ver_productos(request):
    productos = []
    for i in models.Producto.objects.all():
        productos.append(i)
    return render(request, "users/verproductos.html", {"productos": productos})

def view_ver_usuarios(request):
    usuarios = []
    for i in models.Usuario.objects.all():
        usuarios.append(i)
    return render(request, "users/verusuarios.html", {"usuarios": usuarios})

def view_ingresar_compra(request):
    if request.method == "POST":
        form = forms.ComprasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compra ingresada.")
            return redirect("/managermenu")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/managermenu/ingresocompras")
    else:
        form = forms.ComprasForm()
    return render(request, "users/ingresocompras.html", {"form": form})

def view_ver_compras(request):
    compras = []
    for i in models.Compras.objects.all():
        compras.append(i)
    return render(request, "users/vercompras.html", {"compras": compras})

def view_buscar_producto(request):
    if request.method == "GET":
        form = forms.ProductoBuscarForm()
        return render(request, "users/buscarproducto.html", {"form": form})
    else:
        formulario = forms.ProductoBuscarForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto_filtrado = []
            for producto in models.Producto.objects.filter(producto=data["producto"]):
                producto_filtrado.append(producto)
            return render(request, "users/verproductos.html", {"productos": producto_filtrado})
        
def view_buscar_test1(request): #busqueda de IntegerField con choices en models, es ChoiceField en forms
    if request.method == "GET":
        form = forms.Test1Form()
        return render(request, "users/producto_x_categoria.html", {"form": form})
    else:
        formulario = forms.Test1Form(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto_filtrado = []
            for producto in models.Producto.objects.filter(categoria=data["categoria"]): #el primer argumento del paréntesis es el campo a comparar en models y el segundo es el del forms
                producto_filtrado.append(producto)
            return render(request, "users/verproductos.html", {"productos": producto_filtrado})

def view_buscar_test2(request): #busqueda de un campo que es foráneo de otra clase
    if request.method == "GET":
        form = forms.Test2Form()
        return render(request, "users/compras_x_usuario.html", {"form": form})
    else:
        formulario = forms.Test2Form(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            compras_filtrado = []
            aux = get_object_or_404(models.Usuario,nombre=data["usuario"])
            id = aux.pk
            for compra in models.Compras.objects.filter(usuario=id):
                compras_filtrado.append(compra)
            return render(request, "users/vercompras.html", {"compras": compras_filtrado})



































"""def view_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
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
    return render(request, "registration/login.html", {"form": form})"""
    
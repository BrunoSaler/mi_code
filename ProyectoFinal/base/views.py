from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import date
from . import models, forms
from django.contrib.auth.models import User

ruta=None

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
    imagen = info.imagen
    valores_iniciales = {"titulo": info.titulo, "cuerpo": info.cuerpo, "imagen": info.imagen}
    if request.method == 'POST':
        form = forms.EditInfoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            info.titulo = data["titulo"]
            info.cuerpo = data["cuerpo"]
            if (data["imagen"]==None):
                info.imagen = imagen
            else:
                info.imagen = data["imagen"]
            info.save()
            messages.success(request, "Reseña modificada.")
            return redirect("productlist")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("productlist")
    else:
        form = forms.EditInfoForm(initial=valores_iniciales)
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
    return render(request, "base/vercomprasadmin.html", diccionario)

@login_required
def view_perfil(request):
    usuario = request.user
    avatar = models.Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    diccionario = {
        'avatar_url': avatar_url,
        "usuario": usuario,
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
        
@login_required
def view_crear_blog(request):
    if request.method == "POST":
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            subtitulo = form.cleaned_data['subtitulo']
            descripcion = form.cleaned_data['descripcion']
            autor = User.objects.get(id=request.user.id)
            fecha = timezone.now()
            blog = models.Blog(titulo=titulo, subtitulo=subtitulo, descripcion=descripcion, autor=autor, fecha=fecha)
            blog.save()
            return redirect("/menu/all_blogs_admin")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/all_blogs_admin")
    else:
        form = forms.BlogForm()
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
    return render(request, "base/newblog.html", diccionario)

@login_required
def view_ver_blogs_admin(request):
    blogs = []
    for i in models.Blog.objects.all():
        blogs.append(i)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "blogs": blogs,
    }
    return render(request, "base/ver_blogs_admin.html", diccionario)

@login_required
def view_ver_blogs(request):
    blogs = []
    for i in models.Blog.objects.all():
        blogs.append(i)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "blogs": blogs,
    }
    return render(request, "base/ver_blogs.html", diccionario)

@login_required
def view_detailblog_admin(request,id):
    blog = models.Blog.objects.get(id=id)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "blog": blog,
    }
    return render(request, "base/ver_detailblog_admin.html", diccionario)

@login_required
def view_detailblog(request,id):
    blog = models.Blog.objects.get(id=id)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "blog": blog,
    }
    return render(request, "base/ver_detailblog.html", diccionario)

@login_required
def view_edit_blog(request, id):
    blog = models.Blog.objects.get(id=id)
    valores_iniciales = {"titulo": blog.titulo, "subtitulo": blog.subtitulo, "descripcion": blog.descripcion}
    if request.method == "GET":
        form = forms.BlogEditForm(initial=valores_iniciales)
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
        return render(request,"base/editar_blog.html", diccionario)
    else:
        form = forms.BlogEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            blog.titulo = informacion["titulo"]
            blog.subtitulo = informacion["subtitulo"]
            blog.descripcion = informacion["descripcion"]
            fecha = timezone.now()
            blog.save()
            messages.success(request, "Blog editado.")
            return redirect("/menu/all_blogs_admin")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/all_blogs_admin")
        
@login_required
def view_deleteblog(request, id):
    blog = models.Blog.objects.get(id=id)
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
        try:
            blog.delete()
            messages.success(request, "Blog eliminado.")
            return redirect("/menu/all_blogs_admin")
        except:   
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/all_blogs_admin")
    return render(request, "base/borrar_blog.html", diccionario)

@login_required
def view_crear_post(request,id):
    blog = models.Blog.objects.get(id=id)
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = blog
            titulo = form.cleaned_data['titulo']
            subtitulo = form.cleaned_data['subtitulo']
            fecha = timezone.now()
            cuerpo = form.cleaned_data['cuerpo']
            imagen = form.cleaned_data['imagen']
            post = models.Post(blog=blog, titulo=titulo, subtitulo=subtitulo, fecha=fecha, cuerpo=cuerpo, imagen=imagen)
            post.save()
            messages.success(request, "Post creado correctamente.")
            return redirect("/menu/all_blogs_admin")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/all_blogs_admin")
    else:
        form = forms.PostForm()
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
    return render(request, "base/newpost.html", diccionario)

@login_required
def view_verposts_admin(request,id):
    blog = models.Blog.objects.get(id=id)
    posts = []
    comentarios = []  
    for i in models.Post.objects.filter(blog=blog):
        posts.append(i)    
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "posts": posts,
        "comentarios": comentarios,
    }
    return render(request, "base/ver_posts_admin.html", diccionario)

@login_required
def view_verposts(request,id):
    blog = models.Blog.objects.get(id=id)
    posts = []   
    for i in models.Post.objects.filter(blog=blog):
        posts.append(i)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "posts": posts,
    }
    return render(request, "base/ver_posts.html", diccionario)

@login_required
def view_editar_post(request, id):
    post = models.Post.objects.get(id=id)
    imagen = post.imagen
    valores_iniciales = {"titulo": post.titulo, "subtitulo": post.subtitulo, "cuerpo": post.cuerpo, "imagen": imagen}
    if request.method == "POST":
        form = forms.PostEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            post.titulo = data['titulo']
            post.titulo = data['titulo']
            post.subtitulo = data['subtitulo']
            post.fecha = timezone.now()
            post.cuerpo = data['cuerpo']
            post.imagen = data['imagen']
            if (data['imagen']==None):
                post.imagen = imagen
            else:
                post.imagen = data['imagen']
            post.save()
            messages.success(request, "Post editado correctamente.")
            return redirect("/menu/all_blogs_admin")
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/all_blogs_admin")
    else:
        form = forms.PostEditForm(initial=valores_iniciales)
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
    return render(request, "base/editpost.html", diccionario)

@login_required
def view_deletepost(request, id):
    post = models.Post.objects.get(id=id)
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
        try:
            post.delete()
            messages.success(request, "Post eliminado.")
            return redirect("/menu/all_blogs_admin")
        except:   
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect("/menu/all_blogs_admin")
    return render(request, "base/deletepost.html", diccionario)

@login_required
def view_ver_comentarios(request,id):
    global ruta
    post = models.Post.objects.get(id=id)
    comentarios = []
    ruta = request.path 
    for i in models.Comentario.objects.filter(post=post):
        comentarios.append(i)
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    diccionario = {
        'avatar_url': avatar_url,
        "comentarios": comentarios,
        "id": id,
        "titulo":post.titulo,
    }
    return render(request, "base/ver_comentarios.html", diccionario)

@login_required
def view_crear_comentario(request,id):
    post = models.Post.objects.get(id=id)
    usuario = request.user
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            autor = usuario
            post = post
            fecha = timezone.now()
            comment = form.cleaned_data['comentario']
            comentario = models.Comentario(autor=autor, post=post, fecha=fecha, comentario=comment)
            comentario.save()
            messages.success(request, "Comentario agregado.")
            return redirect(ruta)
        else:
            messages.error(request, "Intentelo nuevamente en unos minutos.")
            return redirect(ruta)
    else:
        form = forms.CommentForm()
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
    return render(request, "base/newcomment.html", diccionario)
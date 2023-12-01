from django.urls import path
from app1.views import *

urlpatterns = [
    path("", view_bienvenida),
    path("registro/", view_registrar_usuario),
    path("login/", view_login),
    path("managermenu/", view_managermenu),
    path("usermenu/", view_usermenu),
    path("ingresoproducto/", view_ingresar_producto),
    path("verproductos/", view_ver_productos),
    path("verusuarios/", view_ver_usuarios),
    path("ingresocompras/", view_ingresar_compra),
]
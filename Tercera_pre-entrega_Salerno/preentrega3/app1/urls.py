from django.urls import path
from app1.views import *

urlpatterns = [
    path("", view_bienvenida),
    path("registro/", view_registrar_usuario),
    path("login/", view_login),
    path("managermenu/", view_managermenu),
    path("usermenu/", view_usermenu),
    path("managermenu/ingresoproducto/", view_ingresar_producto),
    path("managermenu/verproductos/", view_ver_productos),
    path("managermenu/verusuarios/", view_ver_usuarios),
    path("managermenu/ingresocompras/", view_ingresar_compra),
    path("managermenu/vercompras/", view_ver_compras),
    path("managermenu/buscarproducto/", view_buscar_producto),
    path("managermenu/producto_x_categoria/", view_buscar_test1),
]
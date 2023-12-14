from django.urls import path
from base.views import *

urlpatterns = [
    path("", view_home),
    path("about/", view_about),
    path("list_lb/", view_list_lb),
    path("list_electro/", view_list_electro),
    path("list_info/", view_list_info),
    path("infoprod/<path:modelo>/", view_infoprod), #el path: es para que me acepte los modelos que tengan /
    path("menu/", view_menu, name="menu"),
    path("menu/newproduct", CrearProductoView.as_view()),
    path("menu/productlist", ProductoView.as_view()),
    path("menu/<pk>/editproduct", ModificarProductoView.as_view(),name="edit-product"),
    path("menu/<pk>/deleteproduct", BorrarProductoView.as_view(),name="delete-product"),
]
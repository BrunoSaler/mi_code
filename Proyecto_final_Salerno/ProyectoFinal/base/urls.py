from django.urls import path
from base.views import *

urlpatterns = [
    path("", view_home),
    path("about/", view_about),
    path("list_lb/", view_list_lb),
    path("menu/infoprod/delete/<path:modelo>/", view_infodelete),
    path("list_electro/", view_list_electro),
    path("list_info/", view_list_info),
    path("infoprod/<path:modelo>/", view_infoprod), #el path: es para que me acepte los modelos que tengan /
    path("menu/", view_menu, name="menu"),
    path("menu/infoprod/edit/<path:modelo>/", view_infoprod_edit),
    path("menu/newproduct/", CrearProductoView.as_view()),
    path("menu/productlist/", ProductoView.as_view(), name="productlist"),
    path("menu/<pk>/editproduct/", ModificarProductoView.as_view(),name="edit-product"),
    path("menu/<pk>/deleteproduct/", BorrarProductoView.as_view(),name="delete-product"),
    path("menu/newinfo/", CrearInfoView.as_view(),name="new-info"),
    path("menu/infoprod/<path:modelo>/", view_infoprod_admin),
    path("menu/ingresocompras/", view_ingresar_compra),
    path("menu/vercompras/", view_ver_compras),
    path("menu/vercomprasadmin/", view_ver_compras_admin),
    

]
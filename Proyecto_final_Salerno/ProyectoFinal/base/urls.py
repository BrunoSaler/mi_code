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
    path("menu/newproduct/", CrearProductoView),
    path("menu/productlist/", ProductoView, name="productlist"),
    path("menu/editproduct/<int:id>/", ModificarProductoView, name="edit-product"),
    path("menu/deleteproduct/<int:id>/", BorrarProductoView, name="delete-product"),    
    path("menu/newinfo/", CrearInfoView,name="new-info"),
    path("menu/infoprod/<path:modelo>/", view_infoprod_admin),
    path("menu/ingresocompras/", view_ingresar_compra),
    path("menu/vercompras/", view_ver_compras),
    path("menu/vercomprasadmin/", view_ver_compras_admin),
    path("menu/edit_profile/", view_editar_perfil),
    path("menu/view_profile/", view_perfil),
    path("menu/edit_avatar/", view_avatar),
    path("menu/new_blog/", view_crear_blog),
    path("menu/all_blogs_admin/", view_ver_blogs_admin),
    path("menu/all_blogs/", view_ver_blogs),
    path("menu/detailblog_admin/<int:id>/", view_detailblog_admin, name="detailblog_admin"),
    path("menu/detailblog/<int:id>/", view_detailblog, name="blog_detalle"),
    path("menu/editblog/<int:id>/", view_edit_blog, name="edit-blog"),
    path("menu/deleteblog/<int:id>/", view_deleteblog, name="borrar-blog"),

    
    

]
from django.urls import path
from base.views import *

urlpatterns = [
    path("", view_home),
    path("about/", view_about),
    path("list_lb/", view_list_lb),
    path("list_electro/", view_list_electro),
    path("list_info/", view_list_info),
    path("infoprod/<path:modelo>/", view_infoprod), #el path: es para que me acepte los modelos que tengan /
]
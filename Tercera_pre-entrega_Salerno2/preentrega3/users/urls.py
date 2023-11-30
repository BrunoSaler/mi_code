from django.contrib import admin
from django.urls import path
from . views import view_bienvenida, view_registrar_usuario, view_login

urlpatterns = [
    path('', view_bienvenida),
    path("registro/", view_registrar_usuario),
    path("login/", view_login),
]

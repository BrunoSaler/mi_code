from django.urls import path
from app1.views import view_bienvenida, view_registrar_usuario, view_login

urlpatterns = [
    path('', view_bienvenida),
    path("registro/", view_registrar_usuario),
    path("login/", view_login),
]
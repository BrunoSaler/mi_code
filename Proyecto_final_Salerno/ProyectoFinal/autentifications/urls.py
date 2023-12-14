from django.urls import path
from django.contrib.auth.views import LogoutView
from autentifications.views import *

urlpatterns = [
    path("signup/", view_register),
    path("login/", view_login),
    path("logout/", view_logout),
]
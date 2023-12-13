from django.urls import path
from autentifications.views import *

urlpatterns = [
    path("signup/", view_register),
]
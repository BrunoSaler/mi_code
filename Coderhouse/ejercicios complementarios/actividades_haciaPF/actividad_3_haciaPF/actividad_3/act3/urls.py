from django.urls import path
from act3.views import *

urlpatterns = [
    path('inicio/', view_bienvenida),
]

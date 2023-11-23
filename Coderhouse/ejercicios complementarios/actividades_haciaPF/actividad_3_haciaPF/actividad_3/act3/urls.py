from django.urls import path
from act3.views import *

urlpatterns = [
    path('', view_bienvenida),
    path('autor/', view_autor),
]

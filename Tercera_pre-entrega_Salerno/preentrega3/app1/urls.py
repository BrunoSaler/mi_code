from django.urls import path
from app1.views import view_bienvenida

urlpatterns = [
    path('', view_bienvenida),
]
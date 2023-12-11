from django.urls import path
from base.views import *

urlpatterns = [
    path("", view_home),
    path("about/", view_about),
]
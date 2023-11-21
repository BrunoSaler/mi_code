from django.http import HttpResponse
from django.shortcuts import render

def view_bienvenida(request):
    return render(request, "act3/welcome.html")

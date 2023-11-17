from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_inicio(xx):
    return HttpResponse("Bienvenidos.")

def view_cursos(xx):
    #return HttpResponse("Aqui voy a mostrar mis cursos.")
    return render(xx, "AppCoder/padre.html")
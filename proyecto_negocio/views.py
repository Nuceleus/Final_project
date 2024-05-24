from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenidos a nuestro negocio</h1>")

def nosotros(request):
    return render(request, "paginas/nosotros.html")
def productos(request):
    return render(request, "productos/index.html")
def servicios(request):
    return render(request, "servicios/index.html")
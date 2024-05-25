from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")
def productos(request):
    return render(request, "productos/index.html")
def servicios(request):
    return render(request, "servicios/index.html")
def crear_producto(request):
    return render(request, "productos/crear.html")
def crear_servicio(request):
    return render(request, "servicios/crear.html")
def editar_producto(request):
    return render(request, "productos/editar.html")
def editar_servicio(request):
    return render(request, "servicios/editar.html")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Servicio
from .forms import ProductoForm, ServicioForm

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")


def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/index.html", {"productos": productos})


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/index.html", {"servicios": servicios})


def crear_producto(request):
    formulario_producto = ProductoForm(request.POST or None, request.FILES or None)
    if formulario_producto.is_valid():
        formulario_producto.save()
        return redirect("productos")
    return render(request, "productos/crear.html", {"formulario_producto": formulario_producto})


def crear_servicio(request):
    formulario_servicio = ServicioForm(request.POST or None, request.FILES or None)
    if formulario_servicio.is_valid():
        formulario_servicio.save()
        return redirect("servicios")
    return render(request, "servicios/crear.html" , {"formulario_servicio": formulario_servicio})


def editar_producto(request):
    return render(request, "productos/editar.html")


def editar_servicio(request):
    return render(request, "servicios/editar.html")

def eliminar_producto(request, idproducto):
    producto = Producto.objects.get(idproducto=idproducto)
    producto.delete()
    return redirect("productos")

def eliminar_servicio(request, idservicio):
    servicio = Servicio.objects.get(idservicio=idservicio)
    servicio.delete()
    return redirect("servicios")
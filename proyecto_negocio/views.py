from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Producto, Servicio, Vacante
from .forms import ProductoForm, ServicioForm, VacanteForm

# Create your views here.

# Archivo de migración: 0005_clean_numero_puestos.py

from django.db import migrations

def limpiar_numero_puestos(apps, schema_editor):
    Vacante = apps.get_model('proyecto_negocio', 'Vacante')
    # Convertir los valores de 'n/a' a 0
    Vacante.objects.filter(numero_puestos='n/a').update(numero_puestos=0)
    # Convertir los valores no numéricos en 0
    for vacante in Vacante.objects.all():
        try:
            vacante.numero_puestos = int(vacante.numero_puestos)
            vacante.save()
        except ValueError:
            vacante.numero_puestos = 0
            vacante.save()

class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_negocio', '0004_remove_vacante_empresa_remove_vacante_estudios_and_more'),
    ]

    operations = [
        migrations.RunPython(limpiar_numero_puestos),
    ]


#Agregado por Jose
def eliminar_vacante(request, id):
    """Elimina la vacante con el ID proporcionado."""
    if request.method == 'POST':
        vacante = get_object_or_404(Vacante, id=id)
        vacante.delete()
        messages.success(request, 'La vacante ha sido eliminada correctamente.')
    # Cambia 'nombre_de_tu_vista_principal' por la vista principal, por ejemplo, 'lista_vacantes'
    return redirect('lista_vacantes')



#Agregado por Jose
def lista_vacantes(request):
    ciudad = request.GET.get('ciudad')
    vacantes = Vacante.objects.all()

    if ciudad:
        vacantes = vacantes.filter(ciudad=ciudad)

    return render(request, 'vacantes/lista.html', {'vacantes': vacantes, 'ciudad': ciudad})

def agregar_vacante(request):
    if request.method == 'POST':
        form = VacanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vacantes')  # Redirige a la lista de vacantes
    else:
        form = VacanteForm()
    return render(request, 'vacantes/agregar_vacante.html', {'form': form})

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


def editar_producto(request, idproducto):
    producto = Producto.objects.get(idproducto=idproducto)
    formulario_producto = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario_producto.is_valid() and request.POST:
        formulario_producto.save()
        return redirect("productos")
    return render(request, "productos/editar.html", {'formulario_producto':formulario_producto})


def editar_servicio(request, idservicio):
    servicio = Servicio.objects.get(idservicio=idservicio)
    formulario_servicio = ServicioForm(request.POST or None, request.FILES or None, instance=servicio)
    if formulario_servicio.is_valid() and request.POST:
        formulario_servicio.save()
        return redirect("servicios")
    return render(request, "servicios/editar.html", {'formulario_servicio':formulario_servicio})

def eliminar_producto(request,idproducto):
    producto = Producto.objects.get(idproducto=idproducto)
    producto.delete()
    return redirect("productos")

def eliminar_servicio(request,idservicio):
    servicio = Servicio.objects.get(idservicio=idservicio)
    servicio.delete()
    return redirect("servicios")
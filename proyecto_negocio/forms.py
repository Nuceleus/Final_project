from django import forms
from .models import Producto, Servicio, Vacante

#Agregado por Jose

class VacanteForm(forms.ModelForm):
    class Meta:
        model = Vacante
        fields = '__all__'  # O especifica los campos que quieres mostrar en el formulario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        
class VacanteForm(forms.ModelForm):
    class Meta:
        model = Vacante
        fields = ['cargo', 'ciudad', 'numero_puestos', 'tiempo_experiencia', 'nivel_estudios', 'modalidad_trabajo', 'rango_salarial', 'descripcion_vacante']

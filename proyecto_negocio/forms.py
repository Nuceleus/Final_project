from django import forms
from .models import Producto, Servicio

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
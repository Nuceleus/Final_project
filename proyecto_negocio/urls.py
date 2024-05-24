from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
]
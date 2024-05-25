from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_servicio/', views.crear_servicio, name='crear_servicio'),
    path('editar_producto/', views.editar_producto, name='editar_producto'),
    path('editar_servicio/', views.editar_servicio, name='editar_servicio'),

]
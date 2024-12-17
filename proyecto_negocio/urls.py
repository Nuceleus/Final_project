from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_servicio/', views.crear_servicio, name='crear_servicio'),
    path('editar_producto/', views.editar_producto, name='editar_producto'),
    path('editar_servicio/', views.editar_servicio, name='editar_servicio'),
    path('editar_producto/<int:idproducto>', views.editar_producto, name='editar_producto'),
    path('editar_servicio/<int:idservicio>', views.editar_servicio, name='editar_servicio'),
    path('eliminar_producto/<int:idproducto>', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar_servicio/<int:idservicio>', views.eliminar_servicio, name='eliminar_servicio'),
    path('lista_vacantes/', views.lista_vacantes, name='lista_vacantes'), #agregado por Jose
    path('agregar/', views.agregar_vacante, name='agregar_vacante'), #agregado por Jose
    path('eliminar-vacante/<int:id>/', views.eliminar_vacante, name='eliminar_vacante'), #agregado por Jose
    path('editar_vacante/<int:id>/', views.editar_vacante, name='editar_vacante'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
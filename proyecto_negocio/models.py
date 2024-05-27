from django.db import models

# Create your models here

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    producto_nombre = models.CharField(max_length=100)
    producto_descripcion = models.TextField()
    producto_imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    producto_precio= models.PositiveIntegerField()
    producto_inventario = models.PositiveIntegerField()
    
    def __str__(self):
        fila = "descripción: " + self.producto_descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.producto_imagen.storage.delete(self.producto_imagen.name)
        super().delete()

class Servicio(models.Model):
    idservicio = models.AutoField(primary_key=True)
    servicio_nombre = models.CharField(max_length=100)
    servicio_descripcion = models.TextField()
    servicio_imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    servicio_precio = models.PositiveIntegerField()

    def __str__(self):
        fila = "descripción: " + self.servicio_descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.servicio_imagen.storage.delete(self.servicio_imagen.name)
        super().delete()

class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    venta_fecha = models.DateField()
    venta_total = models.PositiveIntegerField()
    
    def __str__(self):
        fila = "fecha: " + self.venta_fecha
        return fila


class DetalleVenta(models.Model):
    iddetalleventa = models.AutoField(primary_key=True)
    idventa = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idproducto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    idservicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    detalle_cantidad = models.PositiveIntegerField()
    detalle_precio = models.PositiveIntegerField()
    
class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=100)
    cliente_email = models.CharField(max_length=100)
    
    def __str__(self):
        fila = "nombre: " + self.cliente_nombre + " email: " + self.cliente_email
        return fila

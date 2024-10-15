from django.db import models

# Create your models here.

class Venta(models.Model):
    tipo_cliente = models.CharField()
    #Espacio para la clave foránea de cliente_mayorista
    fecha_venta = models.DateTimeField()
    tipo_venta = models.CharField()
    forma_pago = models.CharField()
    monto_total = models.DecimalField(max_digits = 10, decimal_places = 2)
    observaciones = models.CharField(max_length = 500)
    #espacio para la clave foránea del empleado que realizó la venta


class Item(models.Model):
    #Espacio para clave foranea que relaciona con el producto
    cantidad = models.DecimalField(max_digits = 10, decimal_places = 2)
    precio_item = models.DecimalField(max_digits = 10, decimal_places = 2)


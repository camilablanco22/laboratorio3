from django.db import models

# Create your models here.

class Venta(models.Model):
    tipo_cliente = models.CharField()
    #cliente_mayorista = models.ForeignKey('cliente_mayorista.ClienteMayorista', on_delete = models.SET_NULL,
    #                                       related_name = 'ventas_cliente_mayorista', blank=True, null=True)
    fecha_venta = models.DateTimeField()
    tipo_venta = models.CharField()
    forma_pago = models.CharField()
    monto_total = models.DecimalField(max_digits = 10, decimal_places = 2)
    observaciones = models.CharField(max_length = 500)
    #empleado = models.ForeignKey('empleado.Empleado', on_delete=models.SET_NULL,
    #                                       related_name = 'ventas_empleado'


class Item(models.Model):
    venta = models.ForeignKey('Venta',on_delete=models.CASCADE, related_name='items_venta')
    #producto = models.ForeignKey('producto.Producto', on_delete=models.SET_NULL, related_name='items_venta_producto')
    cantidad = models.DecimalField(max_digits = 10, decimal_places = 2)
    precio_item = models.DecimalField(max_digits = 10, decimal_places = 2)


from django.db import models

# Create your models here.

class Pedido(models.Model):
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.CharField(max_length=500)
    #proveedor = models.ForeignKey('proveedor.Proveedor',on_delete=models.SET_NULL,related_name='pedidos_proveedor')


class ItemPedido(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unid = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey('Pedido',on_delete=models.CASCADE,related_name='items_pedido')
    #materia_prima = models.ForeignKey('materia_prima.MateriaPrima', on_delete=models.SET_NULL, related_name = 'materia_prima_pedida')


class RecepcionPedido(models.Model):
    fecha_recepcion = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    conforme = models.BooleanField()
    observaciones = models.CharField(max_length=500)
    #proveedor = models.ForeignKey('proveedor.Proveedor',on_delete=models.SET_NULL, related_name='pedidos_recibidos_proveedor')
    #empleado = models.ForeignKey('empleado.Empleado',on_delete=models.SET_NULL, related_name='pedidos_empleado')


class ItemRecibido(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unid = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    recepcion_pedido = models.ForeignKey('RecepcionPedido', on_delete=models.CASCADE, related_name='items_recepcion_pedido')
    # materia_prima = models.ForeignKey('materia_prima.MateriaPrima', on_delete=models.SET_NULL, related_name = 'materia_prima_pedida')
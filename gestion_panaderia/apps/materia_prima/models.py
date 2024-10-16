from django.db import models

# Create your models here.

class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=100)
    cant_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    #proveedor = models.ForeignKey('proveedor.Proveedor', n_delete=models.SET_NULL, related_name='materia_prima_provista')
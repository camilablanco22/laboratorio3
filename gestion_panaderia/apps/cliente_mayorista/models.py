from django.db import models


class ClienteMayorista(models.Model):
    nombre_completo = models.CharField(max_length=100)
    cuit = models.CharField(max_length=13, unique=True)
    activo = models.BooleanField(default=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    domicilio_calle = models.CharField(max_length=100)
    domicilio_numero = models.IntegerField()
    localidad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_completo

    def dar_baja(self):
        self.activo = False
        self.save()

    def modificar(self, nombre=None, calle=None, numero=None, localidad=None, departamento=None):
        if nombre:
            self.nombre_completo = nombre
        if calle:
            self.domicilio_calle = calle
        if numero:
            self.domicilio_numero = numero
        if localidad:
            self.localidad = localidad
        if departamento:
            self.departamento = departamento
        self.save()

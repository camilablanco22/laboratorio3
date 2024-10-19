from django.db import models


class Empleado(models.Model):
    estado = models.BooleanField(default=True)
    cuit = models.CharField(max_length=13, unique=True)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_incorporacion = models.DateField()
    domicilio_calle = models.CharField(max_length=100)
    domicilio_numero = models.IntegerField()
    domicilio_localidad = models.CharField(max_length=50)
    domicilio_departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_completo

    def dar_baja(self):
        self.estado = False
        self.save()

    def modificar(self, nombre=None, email=None, calle=None, numero=None, localidad=None, departamento=None):
        if nombre:
            self.nombre_completo = nombre
        if email:
            self.email = email
        if calle:
            self.domicilio_calle = calle
        if numero:
            self.domicilio_numero = numero
        if localidad:
            self.domicilio_localidad = localidad
        if departamento:
            self.domicilio_departamento = departamento
        self.save()

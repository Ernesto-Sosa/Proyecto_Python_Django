from django.db import models

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100)
    carnet_identidad = models.CharField(max_length=11, unique=True)
    chapa_vehiculo = models.CharField(max_length=20)
    modelo_vehiculo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

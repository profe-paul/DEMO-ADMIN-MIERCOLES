from django.db import models



class Producto (models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField()
    oferta = models.BooleanField()
    descripcion = models.TextField(blank=True)


    def __str__(self):
        return self.nombre

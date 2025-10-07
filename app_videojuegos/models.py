from django.db import models

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    anodepublicacion = models.IntegerField()
    genero = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.nombre} ({self.genero})" 
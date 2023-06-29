from django.db import models

from django.contrib.auth.models import User


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.CharField(max_length=255)
    # autor viene de la clase User, RESTRICT - No permite eliminar el usuario si tiene articulos
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    def __str__(self) -> str:
        return self.titulo
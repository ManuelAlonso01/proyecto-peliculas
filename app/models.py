from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    poster = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=500)
    calificacion = models.IntegerField()

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45, unique=True)
    color = models.CharField(max_length=6)
    tamanio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    contacto_duenio = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

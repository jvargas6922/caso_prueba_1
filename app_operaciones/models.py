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

class Procedimiento(models.Model):
    id_procedimiento = models.AutoField(primary_key=True)
    procedimiento = models.CharField(max_length=45)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, db_column='id_sala')
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='id')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, db_column='id_mascota')

    def __str__(self):
        return self.procedimiento


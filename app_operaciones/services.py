from .models import *

#SALA
def listado_salas():
    return Sala.objects.all()

def crear_sala(codigo, color, tamanio, descripcion):
    try:
        sala = Sala(codigo=codigo, color=color, tamanio=tamanio, descripcion=descripcion)
        sala.save()
    except Exception as e:
        return e

def detalle_sala(id):
    try:
        return Sala.objects.get(id_sala=id)
    except Exception as e:
        return e
    
def editar_sala(id, codigo=None, color=None, tamanio=None, descripcion=None):
    try:
        sala = detalle_sala(id)
        if codigo:
            sala.codigo = codigo
        if color:
            sala.codigo = codigo
        if tamanio:
            sala.color = color
        if tamanio:
            sala.tamanio = tamanio
        if descripcion:
            sala.descripcion = descripcion
        sala.save()
    except Exception as e:
        return e
    
def eliminar_sala(id):
    try:
        sala = detalle_sala(id)
        sala.delete()
    except Exception as e:
        return e
    
#MASCOTA

def listado_mascotas():
    return Mascota.objects.all()

def detalle_mascota(id):
    try:
        return Mascota.objects.get(id_mascota=id)
    except Exception as e:
        return e
    
def crear_mascota(nombre, contacto_duenio, especie):
    try:
        mascota = Mascota(nombre=nombre, contacto_duenio=contacto_duenio, especie=especie)
        mascota.save()
    except Exception as e:
        return e
    
def actualizar_mascota(id, nombre=None, contacto_duenio=None, especie=None):
    try:
        mascota = detalle_mascota(id)
        if nombre:
            mascota.nombre = nombre
        if contacto_duenio:
            mascota.contacto_duenio = contacto_duenio
        if especie:
            mascota.especie = especie
        mascota.save()
    except Exception as e:
        return e
    
def eliminar_mascota(id):
    try:
        mascota = detalle_mascota(id)
        mascota.delete()
    except Exception as e:
        return e

#PROCEDIMIENTO

def listado_procedimientos():
    return Procedimiento.objects.all()
 
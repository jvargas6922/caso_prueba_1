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
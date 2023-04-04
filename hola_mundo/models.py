from django.db import models

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100,default="")
    creado_el = models.DateField()
    modificado_el = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.creado_el}"


class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} "
    

class Compras(models.Model):
    articulo = models.TextField(max_length=100)
    precio = models.TextField(max_length=100)
    fecha_de_compra = models.DateField()
    
    def __str__(self):
        return f"{self.id} - {self.articulo} - {self.precio} - {self.fecha_de_compra}"
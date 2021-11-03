from django.db import models

class Cine(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)

class Tipo(models.Model):
    nombre = models.CharField(max_length=200)

class Sala(models.Model):
    numero_sala = models.CharField(max_length=200)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    id_cine = models.ForeignKey(Cine, on_delete=models.CASCADE)

class Fila(models.Model):
    nombre = models.CharField(max_length=200)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

class Clasificacion(models.Model):
    nombre = models.CharField(max_length=200)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=200)
    url_imagen = models.CharField(max_length=200)
    id_clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
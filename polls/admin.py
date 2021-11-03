from django.contrib import admin

from .models import Cine, Sala, Fila, Pelicula, Clasificacion, Tipo

admin.site.register(Cine)
admin.site.register(Sala)
admin.site.register(Fila)
admin.site.register(Pelicula)
admin.site.register(Clasificacion)
admin.site.register(Tipo)

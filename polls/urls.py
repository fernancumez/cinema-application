from django.urls import path

from . import views

urlpatterns = [
    path('', views.listaPeliculas, name='listaPeliculas'),
    path('crearPelicula', views.crearPelicula, name='crearPelicula'),
    path('<int:pelicula_id>/eliminarPelicula', views.eliminarPelicula, name='eliminarPelicula'),
    path('<int:pelicula_id>/actualizarPelicula', views.actualizarPelicula, name='actualizarPelicula')
]
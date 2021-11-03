from django.shortcuts import render, redirect, get_list_or_404
from .models import  Pelicula, Clasificacion, Sala
from .forms import PeliculaForm

def listaPeliculas(request):
   peliculas = Pelicula.objects.all()
   clasificaciones = Clasificacion.objects.all();
   salas = Sala.objects.all();

   context = {
      'peliculas': peliculas,
      'clasificaciones': clasificaciones,
      'salas': salas,
      'form': PeliculaForm()
   }
   
   return render(request, 'polls/pelicula.html',context)


def crearPelicula(request):
   form = PeliculaForm(request.POST)  

   if form.is_valid():  
      try:  
         form.save() 
         return redirect('listaPeliculas')
      except:  
         pass  

   return redirect('listaPeliculas')


def actualizarPelicula(request, id):  
   pelicula = Pelicula.objects.get(id=id)

   print(pelicula)

   form = PeliculaForm(initial={
      'nombre': pelicula.nombre, 
      'sinopsis': pelicula.sinopsis, 
      'id_clasificacion': pelicula.id_clasificacion, 
      'id_sala': pelicula.id_sala}
   )

   if form.is_valid():  
      try:  
         form.save() 
         return redirect('/listaPeliculas')  
      except Exception as e: 
         pass    
   return render(request,'pelicula.html',{'form':form})  


def eliminarPelicula(request, pelicula_id):
   pelicula = Pelicula.objects.get(pk=pelicula_id)
   pelicula.delete()

   return redirect('listaPeliculas')
   
   


   
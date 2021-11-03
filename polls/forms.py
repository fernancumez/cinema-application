from django.db import models
from django.forms import ModelForm
from .models import Pelicula

class PeliculaForm(ModelForm):
   class Meta:
      model = Pelicula
      fields = '__all__'
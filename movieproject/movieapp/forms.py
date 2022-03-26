from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:                       #To include the fields from our model and render it within the same class, we use Meta
        model = Movie
        fields = ['name','image','overview','year','genre','rating']
        
      

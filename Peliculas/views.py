from django.http import HttpResponse
from django.shortcuts import render
from .models import Peliculas  # Asegúrate de tener el modelo correcto

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Peliculas.objects.filter(titulo__icontains=searchTerm)
    else:
        movies = Peliculas.objects.all()
    return render(request, 'home.html', {
        'name': 'Erick Guerrero',
        'searchTerm': searchTerm,
        'movies': movies
    })

def about(request):
    return render(request, 'about.html', {'name': 'Erick Guerrero'})

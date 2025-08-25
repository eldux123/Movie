from django.shortcuts import render
from .models import Peliculas
import matplotlib.pyplot as plt
import io, urllib, base64
from collections import Counter


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


def statistics(request):
    movies = Peliculas.objects.all()

    years = [m.year for m in movies if m.year]  # solo tomamos los que tengan año
    if years:
        plt.figure(figsize=(6, 4))
        plt.hist(years, bins=range(min(years), max(years) + 1), edgecolor="black")
        plt.title("Películas por año")
        plt.xlabel("Año")
        plt.ylabel("Cantidad")
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        graphic = base64.b64encode(buf.read()).decode("utf-8")
        buf.close()
    else:
        graphic = None  # si no hay datos

    # Gráfica por género
    genres = [m.genero.split(",")[0] for m in movies if m.genero]  # solo el primer género
    counts = Counter(genres)
    plt.figure(figsize=(6, 4))
    plt.bar(counts.keys(), counts.values(), color="skyblue")
    plt.xticks(rotation=45)
    plt.title("Películas por género")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    graphic_genre = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    return render(request, 'statistics.html', {
        'graphic': graphic,
        'graphic_genre': graphic_genre
    })


def signup(request):
    email = None
    if request.method == "POST":
        email = request.POST.get("email")
        # Aquí podrías guardar el correo en la BD o hacer otra acción

    return render(request, "signup.html", {"email": email})
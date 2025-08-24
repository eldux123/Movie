from django.core.management.base import BaseCommand
from Peliculas.models import Peliculas
import json
import os

class Command(BaseCommand):
    help = 'Carga 100 películas desde movies.json al modelo Peliculas'

    def handle(self, *args, **kwargs):
        # Dynamically determine the path to movies.json
        json_file_path = os.path.join(os.path.dirname(__file__), 'movies.json')

        # Check if the file exists
        if not os.path.exists(json_file_path):
            self.stderr.write(f"Error: File not found: {json_file_path}")
            return

        # Load the JSON file
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                movies = json.load(file)
        except json.JSONDecodeError as e:
            self.stderr.write(f"Error decoding JSON: {e}")
            return

        # Ensure there are at least 100 movies
        if len(movies) < 100:
            self.stderr.write("Error: The JSON file contains fewer than 100 movies.")
            return

        # Insert movies into the database
        for i in range(100):
            movie = movies[i]["fields"]
            exist = Peliculas.objects.filter(titulo=movie['titulo']).first()
            if not exist:
                try:
                    Peliculas.objects.create(
                        titulo=movie['titulo'],
                        descripcion=movie['descripcion'],
                        fecha_lanzamiento=movie['fecha_lanzamiento'],
                        genero=movie['genero'],
                        year=movie['year'],
                        duracion=movie['duracion'],
                        calificacion=movie['calificacion'],
                        image='peliculas/default.jpg',
                        url=movie['url']
                    )
                except Exception as e:
                    self.stderr.write(f"Error inserting {movie['titulo']}: {e}")
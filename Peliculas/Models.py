from django.db import  models
class Peliculas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=50)
    duracion = models.PositiveIntegerField()  # Duración en minutos
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)  # Calificación de 0.0 a 10.0
    image = models.ImageField(upload_to='peliculas')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.titulo
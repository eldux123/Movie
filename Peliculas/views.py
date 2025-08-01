from django.http import HttpResponse
from django.shortcuts import render


def home(request):
 # return HttpResponse("<h1>Bienvenido a la página principal</h1>") #
 #return render (request, 'home.html')#
 return render (request, 'home.html',{'name': 'Erick Guerrero'})
def about(request):
    return HttpResponse("<h1>Acerca de esta aplicación</h1>")

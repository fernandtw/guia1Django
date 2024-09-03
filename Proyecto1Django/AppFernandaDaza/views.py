from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola, mundo. Esta es la página de inicio de nombreapp</h1>")

def pagina(request):
    return HttpResponse("<h1>Hola, Soy la segunda pagina de esta app</h1>")

# Create your views here.

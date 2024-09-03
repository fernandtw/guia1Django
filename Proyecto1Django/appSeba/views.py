from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola soy el app de index 1</h1>")

def index2(request):
    return HttpResponse("<h1>Hola soy el app de index 2</h1>")

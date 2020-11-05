from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
	return render(request, 'index.html')
def peliculas(request):
	numpeli = Movie.objects.all() 
	return render(request, 'pelis.html', context={"numpeli":numpeli} )
def quienes(request):
	return render(request, 'quienes.html')
def inicio(request):
	return render(request, 'inicio.html')
def registro(request):
	return render(request, 'registro.html')


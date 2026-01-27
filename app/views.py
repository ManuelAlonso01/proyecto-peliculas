from django.shortcuts import render, redirect
from .models import Movies
# Create your views here.


def index(request):
    movies = Movies.objects.all()
    return render(request, 'app/index.html', {"movies": movies})

def subir(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        img = request.POST.get('img')
        descripcion = request.POST.get('descripcion')
        nota = request.POST.get('nota')
        Movies.objects.create(
            title=titulo,
            poster=img,
            descripcion=descripcion,
            calificacion=nota
        )
        return redirect('index')
    return render (request, 'app/subir.html')
    
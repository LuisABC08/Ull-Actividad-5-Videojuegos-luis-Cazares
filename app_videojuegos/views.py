from django.shortcuts import render
from .models import Videojuego

def index(request):
    videojuegos = Videojuego.objects.all()
    # Cambia 'Videojuego' por 'videojuegos' (o el nombre que prefieras para usar en el template)
    return render(request, 'index.html', {'videojuegos': videojuegos})

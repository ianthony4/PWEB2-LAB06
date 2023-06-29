from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.nombreCiudad = 'Cuzco'
    dest1.descipcionCiudad = 'Donde la historia se entrelaza con la grandeza de los Andes.'
    dest1.priceTour = 1500
    dest1.imagenCiudad = 'destination1.jpg'
    dest1.ofertaTour = True
    dest2 = Destination()
    dest2.nombreCiudad = 'Chivay'
    dest2.descipcionCiudad = 'Donde la serenidad se encuentra en los paisajes de los cañones profundos.'
    dest2.priceTour = 1200
    dest2.imagenCiudad = 'destination2.jpg'
    dest2.ofertaTour = False
    dest3 = Destination()
    dest3.nombreCiudad = 'Puno'
    dest3.descipcionCiudad = 'Donde el misterio del lago Titicaca se despliega en todo su esplendor'
    dest3.priceTour = 800
    dest3.imagenCiudad = 'destination3.jpg'
    dest3.ofertaTour = False

    dests = [dest1,dest2,dest3]
    return render(request,'index.html', {'dests': dests})

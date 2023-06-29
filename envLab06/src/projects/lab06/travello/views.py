from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Cuzco'
    dest1.desc = 'Donde la historia se entrelaza con la grandeza de los Andes.'
    dest1.price = 1500
    dest1.img = 'destination1.jpg'
    dest2 = Destination()
    dest2.name = 'Chivay'
    dest2.desc = 'Donde la serenidad se encuentra en los paisajes de los cañones profundos.'
    dest2.price = 1200
    dest2.img = 'destination2.jpg'
    dest3 = Destination()
    dest3.name = 'Puno'
    dest3.desc = 'Donde el misterio del lago Titicaca se despliega en todo su esplendor'
    dest3.price = 800
    dest3.img = 'destination3.jpg'

    dests = [dest1,dest2,dest3]
    return render(request,'index.html', {'dests': dests})

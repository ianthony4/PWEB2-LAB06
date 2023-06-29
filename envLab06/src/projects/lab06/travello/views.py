from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'prueba1'
    dest1.desc = 'Esta ciudad sera una ciudad de peru'
    dest1.price = 700
    return render(request,'index.html', {'dest1': dest1})

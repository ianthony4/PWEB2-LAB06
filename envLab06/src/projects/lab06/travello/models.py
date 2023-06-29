from django.db import models

# Create your models here.

class Destination:
    idCiudad: int
    nombreCiudad: str
    imagenCiudad: str
    descipcionCiudad: str
    priceTour: int
    ofertaTour : bool
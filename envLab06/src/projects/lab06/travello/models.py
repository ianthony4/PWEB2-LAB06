from django.db import models

# Create your models here.

class Destination(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    imagenCiudad =  models.ImageField(upload_to='pics')
    descipcionCiudad = models.TextField()
    priceTour = models.IntegerField
    ofertaTour = models.BooleanField(default=False)
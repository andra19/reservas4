from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class restaurante(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='restaurant_pics')
    nombre = models.CharField(max_length=100)
    rating = models.IntegerField
    ubicacion = models.CharField(max_length=200)
    horarios = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fumar = models.CharField(max_length=100)
    WIFI = models.CharField(max_length=100)
    estacionamiento = models.CharField(max_length=100)
    tarjetas = models.CharField(max_length=100)
    tipoComida = models.CharField(max_length=100)
    comentarios = models.TextField(max_length=500)

    

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurante = models.ForeignKey(restaurante, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(default=1)
    email = models.EmailField(max_length=100)
    personas = models.IntegerField(default=1)
    dia = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detalles', kwargs={'pk': self.pk})

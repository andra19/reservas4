from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class restaurante(models.Model):
    
    OPCIONES = (
         ('Si', 'Si'),
         ('No', 'No'),
     )
    TIPOCOMIDA = (
        ('Vegana', 'Vegana'),
        ('Pastas', 'Pastas'),
        ('Parrilla', 'Parrilla'),
    )
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='restaurant_pics')
    nombre = models.CharField(max_length=100)
    rating = models.IntegerField(null=True)
    ubicacion = models.CharField(max_length=200)
    horarios = models.CharField(max_length=100)
    telefono_restaurante = models.CharField(max_length=100)
    email_restaurante = models.EmailField(max_length=100)
    fumar = models.CharField(max_length=20, choices=OPCIONES)
    wifi = models.CharField(max_length=20, choices=OPCIONES)
    estacionamiento = models.CharField(max_length=20, choices=OPCIONES)
    tarjetas = models.CharField(max_length=20, choices=OPCIONES)
    tipoComida = models.CharField(max_length=100, choices=TIPOCOMIDA)
    comentarios = models.TextField(max_length=500)
    mesa= models.IntegerField(null=True)
   
   


    def __str__(self):
        return self.nombre


    def get_absolute_url(self):
        return reverse('detalles', kwargs={'pk': self.pk})
   

class Reserva(models.Model):
    User= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurante = models.ForeignKey(restaurante, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(default=1)
    email = models.EmailField(max_length=100)
    personas = models.IntegerField(default=1)
    dia = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    mesa= models.IntegerField(null=True)
    
    def get_absolute_url(self):
        return reverse('reserva-delete', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('final', kwargs={'pk': self.pk})
   
    def __str__(self):
        return self.User

    class Meta:
      get_latest_by = 'mesa'

    def reservamesa(request, mesa):
        mesa = restaurante.objects.filter(mesa)
        if mesa == mesa:
            return print("No hay mesas disponibles")
        else:
            mesa = restaurante.objects.create(mesa)


class menu(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    #foto = models.ImageField()
    ingredientes = models.TextField(max_length=200)
  #  tipo = models.ManyToManyField(restaurante, choices=restaurante.TIPOCOMIDA)

    def __str__(self):
        return self.nombre

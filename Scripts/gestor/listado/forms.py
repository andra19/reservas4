from django import forms
from .models import Reserva

class NuevaReserva (forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('nombre', 'apellido', 'email', 'telefono', 'personas', 'dia', 'hora', 'restaurante', 'usuario' )
        widgets = {'restaurante': forms.HiddenInput(), 'usuario': forms.HiddenInput()}
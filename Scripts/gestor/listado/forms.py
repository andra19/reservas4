from django import forms
from .models import Reserva, restaurante

class NuevaReserva (forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ('User', 'email', 'telefono', 'personas', 'dia', 'hora', 'mesa' )
        widgets = {'User':forms.HiddenInput(),'restaurante': forms.HiddenInput(),
        'dia':forms.DateInput,'hora':forms.TimeInput}
from django import forms
from .models import Vuelo

class FormVueloCustom(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Vuelo
        fields = ('origen', 'destino', 'duracion')
from django import forms
from .models import Mecanico

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['nombre', 'carnet_identidad', 'chapa_vehiculo', 'modelo_vehiculo']

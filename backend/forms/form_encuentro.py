from django import forms
from ..models import InscripcionEncuentroBrigada

class InscripcionEncuentroForm(forms.ModelForm):    
    
    class Meta:
        model = InscripcionEncuentroBrigada
        fields = '__all__'    
        labels = {
            'nombre_a_cargo': 'Nombre persona a cargo',
        }
        widgets = {
                'telefono': forms.TextInput(attrs={'placeholder': '912341234'}),
                'email': forms.TextInput(attrs={'placeholder': 'xxxx@gmail.com'}),
        }

            
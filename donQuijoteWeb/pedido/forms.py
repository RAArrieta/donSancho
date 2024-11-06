from django import forms
from . import models

class FormaEntregaForm(forms.ModelForm):
    class Meta:
        model = models.FormaEntrega
        fields = ['forma_entrega', 'precio']
        widgets = {
            "forma_entrega": forms.TextInput(attrs={"class": "form-control"}),
            'precio': forms.NumberInput(attrs={'step': 'any', "class": "form-control"})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['forma_entrega'].disabled = True 
        

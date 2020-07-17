from django import forms
from .models import Animal

SPECIES_CHOICES = [
    ('dog', 'Pies'),
    ('cat', 'Kot'),
]

SIZE_CHOICES = [
    ('-----', '-----'),
    ('small', 'Mały'),
    ('medium', 'Średni'),
    ('big', 'Duży'),
]


class SearchAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('species', 'size', 'identification_number', 'chip_number', 'name')
        widgets = {
            'species': forms.Select(),
            'size': forms.Select(),
            'identification_number': forms.NumberInput(),
            'chip_number': forms.NumberInput(),
            'name': forms.TextInput(),
        }

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
            'species': forms.Select(attrs={

            }),
            'size': forms.Select(attrs={

            }),
            'identification_number': forms.NumberInput(attrs={

            }),
            'chip_number': forms.NumberInput(attrs={

            }),
            'name': forms.TextInput(attrs={

            }),
        }

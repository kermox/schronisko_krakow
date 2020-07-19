from django import forms
from .models import Animal

SPECIES_CHOICES = [
    ('', '-----'),
    ('dog', 'Pies'),
    ('cat', 'Kot'),
]

SIZE_CHOICES = [
    ('', '-----'),
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
            'identification_number': forms.TextInput(),
            'chip_number': forms.TextInput(),
            'name': forms.TextInput(),
        }
        # Pamiętać rzeby po stronie back endu dodać walidację do identification number i chip number

    name = forms.CharField(
        required=False,
    )
    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        required=False,
    )
    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        required=False,
    )


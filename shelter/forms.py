from django import forms

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


class SearchAnimalForm(forms.Form):
    species = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SPECIES_CHOICES,
        required=False
    )
    size = forms.ChoiceField(
        widget=forms.Select,
        choices=SIZE_CHOICES,
        required=False
    )
    identification_number = forms.IntegerField(
        min_value=0,
        required=False
    )
    chip_number = forms.IntegerField(
        min_value=0,
        required=False
    )
    name = forms.CharField(
        max_length=50,
        required=False
    )

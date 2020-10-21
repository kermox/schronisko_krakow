from django import forms

from .models import Animal

SPECIES_CHOICES = [
    ('dog', 'Pies'),
    ('cat', 'Kot'),
]

SIZE_CHOICES = [
    ('small', 'Mały'),
    ('medium', 'Średni'),
    ('big', 'Duży'),
]

AGE_CHOICES = [
    (0, '0-1'),
    (1, '1-3'),
    (2, '3-5'),
    (3, '5+'),
]

GENDER_CHOICES = [
    ('male', 'Samiec'),
    ('female', 'Samica'),
]


class SearchAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('species', 'size', 'identification_number', 'chip_number', 'name', 'age', 'gender')
        widgets = {
            'species': forms.RadioSelect(),
            'size': forms.CharField(),
            'identification_number': forms.TextInput(),
            'chip_number': forms.TextInput(),
            'name': forms.TextInput(),
            'age': forms.RadioSelect(),
        }

    name = forms.CharField(
        required=False,
    )
    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        required=False,
        widget=forms.RadioSelect()
    )
    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        required=False,
        widget=forms.RadioSelect()
    )
    age = forms.ChoiceField(
        choices=AGE_CHOICES,
        required=False,
        widget=forms.RadioSelect(),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=False,
        widget=forms.RadioSelect(),
    )

from django import forms
from .models import EmailBase


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ["address"]
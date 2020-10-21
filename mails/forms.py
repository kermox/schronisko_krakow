from django import forms

from .models import EmailAddress


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ["address"]
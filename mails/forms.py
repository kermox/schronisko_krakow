from django import forms
from .models import EmailBase


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailBase
        fields = ["email_address"]
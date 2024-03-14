from .models import ContactRequest
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
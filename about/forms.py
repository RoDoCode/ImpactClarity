from django import forms
from .models import Resource


class ResourceForm(forms.ModelForm):
    
    class Meta:
        model = Resource
        fields = ['title', 'name_1', 'url_1', 'name_2', 'url_2']

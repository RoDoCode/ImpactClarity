from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Series


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=forms.ClearableFileInput
    )
    video = forms.FileField(
        label='Video',
        required=False,
        widget=forms.ClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class SeriesForm(forms.ModelForm):

    class Meta:
        model = Series
        fields = '__all__'

    screenshot_1 = forms.ImageField(
        label='Screenshot',
        required=False,
        widget=forms.ClearableFileInput
    )
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=forms.ClearableFileInput
    )
    video = forms.FileField(
        label='Video',
        required=False,
        widget=forms.ClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['categories'].queryset = categories
        self.fields['categories'].label_from_instance = (
            lambda obj: obj.get_friendly_name()
        )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

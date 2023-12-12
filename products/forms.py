from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products

        fields = ('image', 'title', 'description', 'price', 'copies')
        label = {
            'image': 'Image',
            'title': 'Title',
            'description': 'Description',
            'price': 'Price',
            'copies': 'Copies'
        }
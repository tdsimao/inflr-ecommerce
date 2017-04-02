from django import forms
from registration.forms import RegistrationForm

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'image_url', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Nome do item"}),
            'image_url': forms.TextInput(attrs={'placeholder': "URL da imagem do item"}),
            'description': forms.Textarea(attrs={'rows': 1, 'placeholder': "Descrição do item"}),
        }


class MyRegistrationForm(RegistrationForm):
    pass
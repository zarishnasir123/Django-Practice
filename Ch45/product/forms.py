from django import forms
from .models import Product


#class="field" is the Tailwind input style from z_dev/input.css
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Product name'}),
            'description': forms.Textarea(attrs={'class': 'field', 'rows': 4, 'placeholder': 'Short description (optional)'}),
            'price': forms.NumberInput(attrs={'class': 'field', 'placeholder': 'e.g. 1500.00', 'step': '0.01', 'min': '0'}),
        }

from django import forms
from .models import Product


# A ModelForm builds the form from the model, so name and price are not written twice.
# It also checks the data (name not empty, price is a number) when we call is_valid().
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        # widgets only change how the input looks, here with Bootstrap classes
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price', 'step': '0.01'}),
        }

    # clean_<fieldname>() checks one field. is_valid() calls it by itself.
    # If something is wrong we raise ValidationError, and the message goes to form.errors['name'].
    # If it is fine we must return the value.
    def clean_name(self):
        name = self.cleaned_data['name']   # the spaces at the start and the end are already removed by Django

        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long.')

        # No two products with the same name. iexact ignores capital letters (Mouse = mouse).
        # exclude(pk=self.instance.pk) is for editing: a product is not a copy of itself.
        # (for a new product the pk is None, so nothing is excluded)
        if Product.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('A product with this name already exists.')

        return name

    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')

        return price

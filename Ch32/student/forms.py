from django import forms
from django.core import validators 
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput,
        validators=[validators.MinLengthValidator(4, message='Name must be at least 4 characters')],  # builtin
    )
    email = forms.EmailField(
        widget=forms.EmailInput,
        validators=[validators.RegexValidator(r'@gmail\.com$', message='Only Gmail addresses are allowed')],  # builtin
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[validators.MinLengthValidator(8, message='Password must be at least 8 characters')],  # builtin
    )
    
    
    #custom validator
    def starts_with_capital(value):
      if not value[0].isupper():
        raise ValidationError('Name must start with a capital letter')
    
    name = forms.CharField(validators=[starts_with_capital])
    
    
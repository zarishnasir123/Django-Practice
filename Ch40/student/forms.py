from django import forms
from .models import Student


#ModelForm built from the Student model; form-control is Bootstrap's input style
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. name@example.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

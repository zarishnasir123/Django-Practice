from django import forms
from .models import Student


# A ModelForm builds its fields from the model, so the view only needs form_class = StudentForm.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']

        # How people style forms: every widget gets a css class (and a placeholder) through attrs.
        # 'form-control' is the Bootstrap class for an input, it only has an effect when the
        # Bootstrap css file is linked in the template.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }

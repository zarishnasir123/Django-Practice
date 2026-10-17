from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    confirm_pass = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}
        labels = {'name': 'Enter your name', 'email': 'Enter your email'}
        error_messages = {
            'email' : {'required' : 'Email is required'}
        }
        widgets = {
            'password' : forms.PasswordInput(attrs={'class': 'pwdclass'}),
            'name' : forms.TextInput(attrs={'class': 'myclass', 'placeholder': "enter name"})
        }

    #password and confirm password must be the same
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_pass = cleaned_data.get('confirm_pass')

        if password and confirm_pass and password != confirm_pass:
            self.add_error('confirm_pass', 'Passwords do not match')

        return cleaned_data
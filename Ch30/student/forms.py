from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
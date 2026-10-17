from django import forms


class StudentForm(forms.Form):
    error_css_class = 'error'

    name = forms.CharField(error_messages={'required' : 'Name is required'})
    email = forms.EmailField(error_messages={'required' : 'Email is required'}, 
    min_length= 5, max_length=50)
    password = forms.CharField(error_messages={'required' : 'Password is required'}, min_length=5, max_length=50)
    
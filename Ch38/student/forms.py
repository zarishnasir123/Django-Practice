from django import forms
from .models import Profile


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class ProfileForm(forms.ModelForm):
    #radio buttons for gender (the model only stores the text)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'dob': 'Date of Birth',
            'pincode': 'Pin Code',
            'job_city': 'Job City',
            'profile_image': 'Profile Image',
            'my_file': 'Document',
        }
        #bootstrap classes: form-control for inputs, form-select for dropdowns
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'job_city': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'my_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

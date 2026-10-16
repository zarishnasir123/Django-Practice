from django import forms

# class DemoForm(forms.Form):
    
#     Gender_choices = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other')
#     ]
    
#     Interest_choices = [
#         ('tech', 'Technology'),
#         ('art', 'Art'),
#         ('sports', 'Sports')
#     ]
    
#     #basic fields
#     name = forms.CharField()
#     email = forms.EmailField()
#     pin_code = forms.IntegerField()
    
    
#     #Additional field types
#     age = forms.FloatField()
#     date_of_birth = forms.DateField()
#     appointment_time = forms.TimeField()
#     is_subsribed = forms.BooleanField()
#     agree_terms = forms.NullBooleanField()
    
#     #Choice Fields
#     gender = forms.ChoiceField(choices=Gender_choices)
#     interests = forms.MultipleChoiceField(choices= Interest_choices)
    
#     #File and Url fields 
#     profile_image = forms.ImageField()
#     resume = forms.FileField()
#     websites = forms.URLField()
    
#     #Other specialized fields 
#     phone_number = forms.RegexField(regex=r'^\+?\d{10,15}$')
#     password = forms.CharField(widget=forms.PasswordInput)
#     slug = forms.SlugField()

#     #field arguments example
#     ip_address = forms.GenericIPAddressField(protocol='IPv4')
#     rating = forms.IntegerField(min_value=1, max_value=5, help_text='Rate from 1 to 5')


class DemoForm(forms.Form):

    Gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    Interest_choices = [
        ('tech', 'Technology'),
        ('art', 'Art'),
        ('sports', 'Sports')
    ]

    #basic fields
    name = forms.CharField(
        label='Full Name',                          # text shown in the label
        max_length=100,                             # adds maxlength="100" and rejects longer text
        help_text='Enter your legal name here',     # hint shown after the field
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}),  # grey hint inside the box
    )
    email = forms.EmailField(
        label='Email Address',
        disabled=True,                              # greyed out, can't be edited
        initial='student@example.com',              # real starting value; a disabled field needs one
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
    )
    pin_code = forms.IntegerField(
        label='Pin Code',
        min_value=100000,                           # smallest 6-digit number
        max_value=999999,                           # largest 6-digit number
        error_messages={'min_value': 'Pin code must be 6 digits', 'max_value': 'Pin code must be 6 digits'},
        widget=forms.NumberInput(attrs={'placeholder': 'Enter 6-digit pin code'}),
    )


    #Additional field types
    age = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}))
    date_of_birth = forms.DateField(
        label='Date of Birth',
        help_text='Enter your birth date in YYYY-MM-DD format',
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
    )
    appointment_time = forms.TimeField(
        label='Appointment Time',
        widget=forms.TimeInput(attrs={'placeholder': 'HH:MM'}),
    )
    appointment_datetime = forms.DateTimeField(
        label='Appointment Date & Time',
        widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
    )
    is_subsribed = forms.BooleanField(label='Subscribe to Newsletter', required=False)  # checkbox can be left unticked
    agree_terms = forms.NullBooleanField(label='Do you agree with terms?')  # no ':' is added after '?'

    #Choice Fields
    gender = forms.ChoiceField(choices=Gender_choices, widget=forms.RadioSelect)
    interests = forms.MultipleChoiceField(choices=Interest_choices)

    #File and Url fields
    profile_image = forms.ImageField(label='Profile Image')
    resume = forms.FileField()
    websites = forms.URLField(
        label='Website',
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}),
    )

    #Other specialized fields
    phone_number = forms.RegexField(
        label='Phone Number',
        regex=r'^\+?\d{10,15}$',
        error_messages={'invalid': 'Enter 10 to 15 digits'},  # your own error text
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter 8-character password'}),
        min_length=8,                               # not less than 8 characters
        max_length=8,                               # not more than 8 characters
        error_messages={'min_length': 'Password must be exactly 8 characters', 'max_length': 'Password must be exactly 8 characters'},
    )
    slug = forms.SlugField(widget=forms.Textarea(attrs={'placeholder': 'e.g. my-first-post', 'rows': 4, 'cols': 40}))

    #field arguments example
    ip_address = forms.GenericIPAddressField(
        label='IP Address',
        protocol='IPv4',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 192.168.1.1'}),
    )
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        help_text='Rate from 1 to 5',
        widget=forms.NumberInput(attrs={'placeholder': '1 to 5'}),
    )

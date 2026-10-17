from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    # #clean and validate field specific in django forms
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 4:
    #         raise forms.ValidationError("Name must be atleast 4 characters")
        
    #     return name
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if len(email) < 10:
    #         raise forms.ValidationError("Email must be atleast 10 characters")

        # return email
    
    #validation the whole form at once using clean()
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        
        if name and len(name) < 4:
            self.add_error('name','enter more than or equal to 4 characters')

        if email and len(email) < 10:
            self.add_error('email', 'enter more than or equal to 10 characters')

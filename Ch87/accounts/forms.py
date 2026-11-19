from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


# UserCreationForm is Django's sign up form: it asks the password twice, checks both are the same
# and saves it hashed. Here it is pointed at our own user model, and the email is added.
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

    # the login is done with the email, so two users must not have the same one
    # clean_<field name>() runs after that field is checked; raising an error shows it under the box
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        return email


# AuthenticationForm is Django's login form. Its first box is called "username" inside, whatever the
# user model uses to log in (here it is the email, USERNAME_FIELD), so only the label, the kind of box
# and the message change.
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': 'Please enter a correct email and password.',
    }

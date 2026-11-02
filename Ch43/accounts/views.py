from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from .forms import RegistrationForm
from .models import User
from .utils import send_activation_email, send_password_reset_email

# Create your views here.
# these only show the pages; the authentication code goes here later
# (named ..._view so they don't clash with django.contrib.auth's login() when you import it)

def home_view(request):
    return render(request, 'accounts/home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            #commit=False: build the user first, so the password can be hashed before saving
            user = form.save(commit=False)
            is_seller = form.cleaned_data['account_type'] == 'seller'
            user.is_seller = is_seller
            user.is_customer = not is_seller
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_activation_email(request, user)
            messages.success(request, 'Your account has been created. Please check your email to activate your account.')
            return redirect('login')

    else:
        form = RegistrationForm()

    #a new form, or the submitted form with its errors
    return render(request, 'accounts/register.html', {'form': form})


#the link in the email opens this: a valid token sets is_active = True
def activate_view(request, uidb64, token):
    try:
        pk = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=pk)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated. You can now log in.')
    else:
        messages.error(request, 'This activation link is invalid or has expired.')

    return redirect('login')


#a new activation link, for when the old one expired
def resend_activation_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        user = User.objects.filter(email=email, is_active=False).first()

        if user is not None:
            send_activation_email(request, user)

        messages.success(request, 'If that account still needs activating, a new link has been sent.')
        return redirect('login')

    return render(request, 'accounts/resend_activation.html')


def login_view(request):
    email = ''

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        #checks the email and password; gives None if wrong or if the account isn't active
        user = authenticate(request, email=email, password=password)

        if user is not None:
            #login() starts the session (the sessionid cookie)
            login(request, user)

            #go back to the page that asked for login, but only if it's on this site
            next_url = request.POST.get('next', '')
            if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)

            #only-seller accounts go to the seller dashboard, everyone else to the customer one
            if user.is_seller and not user.is_customer:
                return redirect('seller_dashboard')
            return redirect('customer_dashboard')

        #correct password but not activated yet: tell them what to do
        inactive = User.objects.filter(email=email, is_active=False).first()
        if inactive is not None and inactive.check_password(password):
            messages.error(request, 'Please activate your account first. Check your email for the link.')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'accounts/login.html', {'email': email, 'next': request.POST.get('next') or request.GET.get('next', '')})


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        user = User.objects.filter(email=email, is_active=True).first()

        if user is not None:
            send_password_reset_email(user)

        #same message either way, so nobody can test which emails are registered
        messages.success(request, 'If that email has an account, a reset link has been sent.')
        return redirect('login')

    return render(request, 'accounts/forgot_password.html')


#checks that the passwords match and are strong enough; returns a list of error messages
def password_errors(new_password, confirm_password, user):
    if new_password != confirm_password:
        return ["Passwords don't match"]
    try:
        validate_password(new_password, user)
    except ValidationError as error:
        return error.messages
    return []


#finds the user from the uidb64 in an emailed link
def user_from_uid(uidb64):
    try:
        return User.objects.get(pk=urlsafe_base64_decode(uidb64).decode())
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return None


# uidb64 (the user's id) and token come from the link in the email;
# checking that the token is valid is part of the authentication code you'll add
def reset_password_confirm_view(request, uidb64, token):
    user = user_from_uid(uidb64)

    if user is None or not default_token_generator.check_token(user, token):
        messages.error(request, 'This reset link is invalid or has expired.')
        return redirect('forgot_password')

    errors = []

    if request.method == 'POST':
        new_password = request.POST.get('new_password', '')
        errors = password_errors(new_password, request.POST.get('confirm_password', ''), user)

        if not errors:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been reset. You can now log in.')
            return redirect('login')

    return render(request, 'accounts/reset_password_confirm.html', {'errors': errors})


# shared by customers and sellers (both dashboards link here)
@login_required
def change_password_view(request):
    errors = []

    if request.method == 'POST':
        new_password = request.POST.get('new_password', '')

        if not request.user.check_password(request.POST.get('old_password', '')):
            errors = ['Your old password is incorrect.']
        else:
            errors = password_errors(new_password, request.POST.get('confirm_password', ''), request.user)

        if not errors:
            request.user.set_password(new_password)
            request.user.save()
            #keeps the user logged in after the password changes
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Your password has been changed.')
            if request.user.is_seller and not request.user.is_customer:
                return redirect('seller_dashboard')
            return redirect('customer_dashboard')

    return render(request, 'accounts/change_password.html', {'errors': errors})


# the dashboards' "Log out" button posts here; it ends the session and goes back to the login page
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

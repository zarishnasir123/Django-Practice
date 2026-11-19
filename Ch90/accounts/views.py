from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from .forms import LoginForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    # method_decorator on ONE method (here get): never_cache tells the browser not to keep this page,
    # so after logout the back button does not show the page of the logged in user.
    # method_decorator is needed because a decorator expects a view function (request, ...), but a
    # method gets self first. It hides self so that a normal decorator can be used on a method.
    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# LoginView already checks the email and password and logs the user in.
# Only the template, the form (it asks for the email) and the page to go to afterwards are written here.
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

    # each kind of user goes to their own page
    def get_success_url(self):
        user = self.request.user
        if user.is_customer:
            return reverse('customer_dashboard')
        if user.is_seller:
            return reverse('seller_dashboard')
        return reverse('home')


# ---------- change password (the user is logged in and knows the old password) ----------
# These are ready made Django views. Only the template is chosen here, and extra_context sends
# the heading and the button text to the template (one template draws all the forms).
# PasswordChangeView already refuses a visitor who is not logged in.
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/auth_form.html'
    extra_context = {'title': 'Change password', 'button': 'Change password'}
    # the next page is the url named password_change_done (it is the default, so no success_url)


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/auth_message.html'
    extra_context = {
        'title': 'Password changed',
        'message': 'Your password has been changed.',
        'link': reverse_lazy('home'),
        'link_text': 'Go to home',
    }


# ---------- forgot password (the user can not log in, a link is sent by email) ----------
# 1. the visitor types the email -> an email with a link is sent (through Gmail, see settings.py)
# 2. "check your email" page
# 3. the link opens the page where the new password is typed (the link has a token inside it)
# 4. "password changed" page
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/auth_form.html'
    email_template_name = 'accounts/password_reset_email.txt'       # the plain text of the email
    html_email_template_name = 'accounts/password_reset_email.html' # the styled card (the text is kept for programs that can't show it)
    subject_template_name = 'accounts/password_reset_subject.txt'   # the subject of the email
    extra_context = {
        'title': 'Forgot password',
        'text': 'Type the email of your account and we will send you a link to choose a new password.',
        'button': 'Send reset link',
    }


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/auth_message.html'
    extra_context = {
        'title': 'Check your email',
        'message': 'If an account has that email, a link to reset the password was sent to it.',
        'link': reverse_lazy('login'),
        'link_text': 'Back to login',
    }


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/auth_form.html'
    extra_context = {'title': 'Choose a new password', 'button': 'Save password'}


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/auth_message.html'
    extra_context = {
        'title': 'Password changed',
        'message': 'Your password has been changed, you can log in with it now.',
        'link': reverse_lazy('login'),
        'link_text': 'Login',
    }

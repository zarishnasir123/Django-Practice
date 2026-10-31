import threading

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode


#sends in a background thread, so the user doesn't wait for Gmail after clicking Register
class EmailThread(threading.Thread):
    def __init__(self, email):
        super().__init__()
        self.email = email

    def run(self):
        self.email.send()


#emails the user a password reset link; it expires after PASSWORD_RESET_TIMEOUT
def send_password_reset_email(user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_link = settings.SITE_DOMAIN + reverse('reset_password_confirm', args=[uidb64, token])

    body = f'Hi {user.name},\n\nReset your password with this link (it expires in 15 minutes):\n{reset_link}\n\nIf you did not ask for this, you can ignore this email.'
    EmailThread(EmailMultiAlternatives('Reset your password', body, to=[user.email])).start()


#emails the user a link with their id (uidb64) and a token; clicking it opens activate_view
def send_activation_email(request, user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_link = settings.SITE_DOMAIN + reverse('activate', args=[uidb64, token])

    html = render_to_string('accounts/activation_email.html', {'name': user.name, 'activation_link': activation_link})
    #the plain text version is for email apps that don't show HTML
    email = EmailMultiAlternatives('Activate your account', strip_tags(html), to=[user.email])
    email.attach_alternative(html, 'text/html')
    EmailThread(email).start()


from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    # login_required: a visitor who is not logged in is sent to the login page (LOGIN_URL in settings.py)
    path('dashboard/', login_required(TemplateView.as_view(template_name='myapp/dashboard.html')), name='dashboard'),
    # LogoutView only accepts POST, the page to go to afterwards is LOGOUT_REDIRECT_URL in settings.py
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    # template_name chooses our own template instead of the default registration/password_change_form.html
    # PasswordChangeView needs a logged in user, and after saving it goes to the url named password_change_done
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='myapp/password_change.html'), name='password_change'),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(template_name='myapp/password_change_done.html'), name='password_change_done'),
]

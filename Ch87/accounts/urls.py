from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

# The url NAMES of the password views must stay as they are written here: Django's views, and the link
# inside the email, look for them by name (password_reset_done, password_reset_confirm...).
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # LogoutView needs no changes: it logs out (only on a POST) and goes to LOGOUT_REDIRECT_URL
    path('logout/', LogoutView.as_view(), name='logout'),

    # change password with the old password
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    # forgot password, by email
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    # uidb64 = the user id and token = the secret part, both come from the link in the email
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

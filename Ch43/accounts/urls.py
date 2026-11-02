from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    #the link inside the activation email opens this page
    path('activate/<str:uidb64>/<str:token>/', views.activate_view, name='activate'),
    path('resend-activation/', views.resend_activation_view, name='resend_activation'),
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    #the link inside the reset email opens this page, e.g. /reset/MQ/abc123-token/
    path('reset/<str:uidb64>/<str:token>/', views.reset_password_confirm_view, name='reset_password_confirm'),
    #shared by customers and sellers
    path('change-password/', views.change_password_view, name='change_password'),
    path('logout/', views.logout_view, name='logout'),
]

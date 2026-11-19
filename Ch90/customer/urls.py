from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CustomerSignUpView.as_view(), name='customer_signup'),
    path('dashboard/', views.CustomerDashboardView.as_view(), name='customer_dashboard'),
]

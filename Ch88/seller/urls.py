from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SellerSignUpView.as_view(), name='seller_signup'),
    path('dashboard/', views.SellerDashboardView.as_view(), name='seller_dashboard'),
]

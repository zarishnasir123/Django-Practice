from django.contrib.auth import views as auth_view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('public/', views.PublicView.as_view(), name='public'),
    path('login/', auth_view.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    # LogoutView only accepts POST
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]

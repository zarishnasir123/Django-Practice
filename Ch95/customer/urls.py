from django.urls import path
from . import views

# app_name is the namespace of this app: its names are used as customer:dashboard and customer:profile.
# Without it, a name like 'dashboard' here and in seller would clash.
app_name = 'customer'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

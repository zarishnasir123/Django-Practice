from django.urls import path
from . import views

# the namespace of this app: seller:dashboard
# the name 'dashboard' is the same as in customer, and that is fine because of the namespaces
app_name = 'seller'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]

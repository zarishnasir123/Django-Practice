from django.urls import path
from . import views

# core has no app_name, so its names stay plain: {% url 'home' %}
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]

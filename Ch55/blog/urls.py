from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('math/', views.math, name='math'),
    path('user/', views.user, name='user'),
     path('uc/', views.user, name='user'),
]

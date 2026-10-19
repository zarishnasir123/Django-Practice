from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #dynamic url: <int:pk> takes the candidate's id from the address, e.g. /candidate/3/
    path('candidate/<int:pk>/', views.candidate, name='candidate'),
]

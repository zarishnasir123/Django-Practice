from django.urls import path
from . import views

urlpatterns = [
    #register form + list (success / error messages)
    path('', views.home, name='home'),
    #delete a student (warning message)
    path('delete/<int:id>/', views.delete_student, name='delete'),
    #one message of every level
    path('levels/', views.all_levels, name='levels'),
]

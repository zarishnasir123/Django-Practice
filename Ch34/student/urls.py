from django.urls import path
from . import views

urlpatterns = [
    path('student-form/', views.student_form, name='student_form'),
    path('success/', views.success, name='success'),
]
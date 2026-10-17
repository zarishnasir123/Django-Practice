from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_form, name='student_form'),
    path('teacher/', views.teacher_form, name='teacher_form'),
    path('success/', views.success, name='success'),
]

from django.urls import path
from course.views import php_course

urlpatterns = [
    path('php/', php_course, name='php_course'),
]
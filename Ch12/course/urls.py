from django.urls import path, include
from course.views import learn_django

urlpatterns = [
    path('dj/', learn_django)
    
]

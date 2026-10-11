from django.urls import path
from course.views import learn_django, learn_python

urlpatterns = [
    path('dj/', learn_django),
    path('py/', learn_python,)
    
]

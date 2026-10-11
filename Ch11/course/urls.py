from django.urls import path
from course.views import learn_django
from course.views import learn_fasiapi

urlpatterns = [
    path('dj/', learn_django, name='learn_django'),
    path('fast/', learn_fasiapi, name='learn_fasiapi')
]

from django.urls import path
from student.views import registration

urlpatterns = [
    path('register/', registration, name='registration')

]


from django.urls import path
from app2.views import myapp2

urlpatterns = [
    path('app2/', myapp2)
     
]
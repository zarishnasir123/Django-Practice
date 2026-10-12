from django.urls import path, include
from core.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('aboutme/', about, name='about'),
]

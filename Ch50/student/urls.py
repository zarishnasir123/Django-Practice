from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.home, name='home'),
    path('home/',cache_page(60) (views.home), name='home'),
    path('index/', views.home, name='home'),
    
    path('course/', views.course, name='course'),
    path('result/',cache_page(30) (views.result), name='result'),
]

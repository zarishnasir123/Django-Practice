from django.urls import path 
from student import views

urlpatterns = [
    path('set/', views.setcookie),
    path('get/', views.getcookie),
    path('del/', views.delcookie),
    path('setsigned/', views.setsignedcookie),
    path('getsigned/', views.getsignedcookie),
    
]

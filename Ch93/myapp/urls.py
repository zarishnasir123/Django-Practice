from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sync/', views.SyncView.as_view(), name='syncview'),
    path('async/', views.AsyncView.as_view(), name='asyncview'),
]

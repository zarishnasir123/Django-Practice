from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/products/', views.ProductAPI.as_view(), name='products'),
    path('api/products/<int:pk>/', views.ProductDetailAPI.as_view(), name='product_detail'),
]

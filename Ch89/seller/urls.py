from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SellerSignUpView.as_view(), name='seller_signup'),
    path('dashboard/', views.SellerDashboardView.as_view(), name='seller_dashboard'),

    # the seller's products
    path('products/', views.SellerProductListView.as_view(), name='seller_products'),
    path('products/add/', views.SellerProductCreateView.as_view(), name='seller_product_add'),
    path('products/<int:pk>/edit/', views.SellerProductUpdateView.as_view(), name='seller_product_edit'),
    path('products/<int:pk>/delete/', views.SellerProductDeleteView.as_view(), name='seller_product_delete'),
]

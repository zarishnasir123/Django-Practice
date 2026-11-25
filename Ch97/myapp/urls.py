from django.urls import path
from . import views

urlpatterns = [
    # function based views
    path('', views.homeview, name='home'),
    path('products/', views.productlistview, name='productlist'),
    path('products/names/', views.productnamesview, name='productnames'),
    path('products/<int:pk>/', views.productdetailview, name='productdetail'),
    path('created/', views.createdview, name='created'),

    # class based views
    path('class/products/', views.ProductListView.as_view(), name='productlist_class'),
    path('class/products/<int:pk>/', views.ProductDetailView.as_view(), name='productdetail_class'),
]

from django.urls import path
from . import views

# the names are what reverse() and reverse_lazy() look up
urlpatterns = [
    path('home/', views.homeview, name='home'),
    path('product/<int:pk>/', views.productview, name='product'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post')
]

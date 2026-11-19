from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # <int:pk> must be named pk: the UpdateView looks for the row with this pk
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='studentupdate'),
    path('thanks/', TemplateView.as_view(template_name='myapp/thanks.html'), name='thanks'),
]

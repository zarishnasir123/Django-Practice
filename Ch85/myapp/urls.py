from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # <int:pk> must be named pk: the DeleteView looks for the row with this pk
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='studentdelete'),
    path('thanks/', TemplateView.as_view(template_name='myapp/thanks.html'), name='thanks'),
]

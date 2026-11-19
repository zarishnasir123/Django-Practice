from django.urls import path
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='studentcreate'),
    path('thanks/', TemplateView.as_view(template_name='myapp/thanks.html'), name ='thanks')
]

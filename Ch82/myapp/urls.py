from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thanks/', TemplateView.as_view(template_name='myapp/thankyou.html'), name='thanks')
    
]

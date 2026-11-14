from django.urls import path
from . import views
from myapp import views



# urlpatterns = [
#     path('home/', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
# ]

urlpatterns = [
    path('index/', views.TemplateView.as_view(template_name="myapp/index.html"), name='index'),
    path('about/', views.TemplateView.as_view(template_name='myapp/about.html'), name = 'about'),
    # # path('contact/', views.TemplateView.as_view(template_name='myapp/contact.html'), name = 'contact'),
    # path('contact/', views.ContactTemplateView.as_view(extra_context={'course': 'Python'}), name = 'contact'),
    path('profile/<int:id>', views.ProfileTemplateView.as_view(template_name='myapp/profile.html'), name = 'profile'),
    
]


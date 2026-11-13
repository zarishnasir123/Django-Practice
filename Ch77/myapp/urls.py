from django.urls import path
from . import views

urlpatterns = [
    #-------- function based views --------
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # #the third value is a dictionary of extra arguments sent to the view
    # path('news/', views.news, {'template_name': 'news.html'}, name='news'),
    # path('news2/', views.news, {'template_name': 'news2.html'}, name='news2'),

    #-------- class based views: .as_view() --------
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    #news.html is the class default; news2 changes template_name inside as_view()
    path('news/', views.NewsView.as_view(), name='news'),
    path('news2/', views.NewsView.as_view(template_name='myapp/news2.html'), name='news2'),
]

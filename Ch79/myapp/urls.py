from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    #-------- normal pages --------
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('news/<int:id>/', views.NewsView.as_view(), name='news'),
    path('results/', views.ResultsView.as_view(), name='results'),

    #-------- redirects --------
    #url=: a fixed address (302 by default)
    path('go-home/', RedirectView.as_view(url='/'), name='go_home'),

    #pattern_name=: the NAME of a url, so the address can change without breaking this;
    #permanent=True sends a 301, which tells browsers and search engines the move is for good
    path('old-about/', RedirectView.as_view(pattern_name='about', permanent=True), name='old_about'),

    #URL values (here id) are passed on to the target url
    path('old-news/<int:id>/', views.OldNewsRedirectView.as_view(), name='old_news'),

    #query_string=True keeps ?q=django on the new address
    path('old-search/', RedirectView.as_view(pattern_name='results', query_string=True), name='old_search'),

    #a class that works out the address itself
    path('latest-news/', views.LatestNewsRedirectView.as_view(), name='latest_news'),

    #an address on another website
    path('django-site/', RedirectView.as_view(url='https://www.djangoproject.com/'), name='django_site'),
]

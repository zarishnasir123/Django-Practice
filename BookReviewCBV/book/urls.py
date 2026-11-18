from django.urls import path
from django.views.generic import RedirectView
from . import views

#these names are used by the templates ({% url 'book_list' %} ...) and by Book.get_absolute_url()
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('add/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    #redirects
    path('latest/', views.LatestBookRedirectView.as_view(), name='book_latest'),
    path('random/', views.RandomBookRedirectView.as_view(), name='book_random'),
    #an old address kept working: /books/ moves for good (301) to the list
    path('books/', RedirectView.as_view(pattern_name='book_list', permanent=True)),
]

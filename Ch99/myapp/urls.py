from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-count/', views.book_count_view, name='book_count'),
    path('many-books/', views.many_books_view, name='many_books'),
    path('no-books/', views.no_books_view, name='no_books'),
    path('price-report/', views.price_report_view, name='price_report'),
    path('discount-count/', views.discount_count_view, name='discount_count'),
    path('expensive-authors/', views.expensive_authors_view, name='expensive_authors'),
    path('author-books/', views.author_books_view, name='author_books'),
]

from django.urls import path
from . import views

urlpatterns = [
    #READ: all books
    path('', views.home, name='home'),
    #CREATE: add a book (staff only)
    path('book/add/', views.add_book, name='add_book'),
    #READ: one book's page; Book.get_absolute_url() points here by the name 'book_detail'
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    #UPDATE: edit a book (staff only)
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    #DELETE: confirm and delete a book (staff only)
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    #write a review for this book (logged-in users only)
    path('book/<int:pk>/review/', views.add_review, name='add_review'),
]

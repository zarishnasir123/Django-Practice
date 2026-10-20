from django.contrib import admin
from .models import Book, Review

# Register your models here.

#shows a book's reviews as rows inside the book's admin page
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0    #no empty extra rows; use "Add another Review" when needed


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #columns in the list (average_rating is the method from models.py)
    list_display = ('id', 'title', 'author', 'genre', 'published_year', 'average_rating', 'created_at')
    #filter box on the right side
    list_filter = ('genre',)
    #search box at the top
    search_fields = ('title', 'author')
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    #book__title / user__username: search inside the linked book and user
    search_fields = ('book__title', 'user__username', 'comment')

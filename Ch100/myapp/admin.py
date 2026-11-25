from django.contrib import admin
from .models import Author, Book, Tag

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'price', 'discount']
    # a many to many field is shown as two boxes (all tags / chosen tags) in the edit page
    filter_horizontal = ['tags']

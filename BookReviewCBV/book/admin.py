from django.contrib import admin
from django.utils.html import format_html
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'cover', 'title', 'author', 'genre', 'isbn', 'publication_date', 'average_rating', 'created_at', 'updated_at']
    list_filter = ['genre']
    search_fields = ['title', 'author', 'isbn']
    #created_at and updated_at are set automatically, so they can be seen but not edited
    readonly_fields = ['created_at', 'updated_at']

    @admin.display(description='Cover')
    def cover(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height: 48px; border-radius: 4px;">', obj.cover_image.url)
        return '-'

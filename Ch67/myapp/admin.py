from django.contrib import admin
from .models import Page, Post, Song

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pname', 'pcat', 'ppublished']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'post', 'ptpublished']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    #a ManyToManyField can't go straight into list_display, so written_by joins the usernames
    list_display = ['id', 'stitle', 'sduration', 'written_by']
    filter_horizontal = ['user']

    def written_by(self, obj):
        return ", ".join([str(u) for u in obj.user.all()])

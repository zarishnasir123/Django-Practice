from django.contrib import admin
from myapp.models import Profile, Page, Like

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'page_name']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['page', 'page_name', 'likes']

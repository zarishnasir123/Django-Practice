from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# UserAdmin is Django's admin for users (it hashes the password for us). It is written for the normal
# user, so its sections are repeated here with our own fields (no groups or permissions).
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'is_customer', 'is_seller', 'is_staff']
    list_filter = ['is_customer', 'is_seller', 'is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['email']
    filter_horizontal = []   # UserAdmin lists groups and permissions here, this user has none

    # the page that edits a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Role', {'fields': ('is_customer', 'is_seller')}),
        ('Access', {'fields': ('is_active', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # the page that adds a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'usable_password', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

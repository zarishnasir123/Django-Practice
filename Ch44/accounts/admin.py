from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'city', 'is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller', 'is_seller_approved')
    list_filter = ('is_active', 'is_staff', 'is_customer', 'is_seller')
    search_fields = ('email', 'name')
    #the password is stored as a hash, so show it read-only instead of as an editable box
    readonly_fields = ('password', 'last_login', 'created_at', 'updated_at')

    #groups the fields into sections on the user's admin page
    fieldsets = (
        ('Login info', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'city')}),
        ('Roles', {'fields': ('is_customer', 'is_seller', 'is_seller_approved')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

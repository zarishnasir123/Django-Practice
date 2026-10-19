from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'gender', 'locality', 'city', 'pincode', 'state',
                    'mobile', 'email', 'job_city', 'profile_image', 'my_file')

from django.contrib import admin
from student.models import Profile,Result

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'roll', 'email', 'city')
    
admin.site.register(Profile,ProfileAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('stu_class', 'marks')

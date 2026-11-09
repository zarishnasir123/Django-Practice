from atexit import register

from django.contrib import admin
from school.models import Student, Teacher, Contractor, ExamCenter, Candidate, Product, DiscountedProduct

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary', 'join_date']


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'payment', 'join_date']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'center_name', 'center_city']


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['center_name', 'center_city']
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'stock']
    


@admin.register(DiscountedProduct)
class DiscountedProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock']
    
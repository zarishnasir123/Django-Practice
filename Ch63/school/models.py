from django.db import models
from school.managers import CustomStudentManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admdate = models.DateField()

    # students = models.Manager()
    
    objects = CustomStudentManager()
    
# class ProxyStudent(Student):
#     students = CustomStudentManager()
#     class Meta:
#         proxy = True 
#         ordering = ['name']
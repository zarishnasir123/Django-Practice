from django.db import models

class Person(models.Model):
    student_name = models.CharField(max_length=70)
    teacher_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

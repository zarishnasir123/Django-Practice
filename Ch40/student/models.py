from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    #unique=True: a second student with the same email fails validation (used for the error message example)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

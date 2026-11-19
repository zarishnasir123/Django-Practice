from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    # after a valid update the UpdateView goes here (the thanks page)
    def get_absolute_url(self):
        return reverse('thanks')

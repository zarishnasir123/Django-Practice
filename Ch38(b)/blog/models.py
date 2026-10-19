from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field()

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, 
    # limit_choices_to={'is_staff' : True})
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Page(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=255)
    
class Like(Page):
    #parent_link=True: this field IS the link to the parent Page (instead of the automatic page_ptr)
    page = models.OneToOneField(Page, on_delete=models.CASCADE, parent_link=True, primary_key=True)
    likes = models.IntegerField()
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#many to many: one user can have many songs, and one song can belong to many users
#Django makes a third table (myapp_song_user) that stores the user-song pairs
class Song(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=255)
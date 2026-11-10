from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pname = models.CharField('Page name',max_length=255)
    pcat = models.CharField('page category',max_length=255)
    ppublished = models.DateField()
    
class Post(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField('Post Title',max_length=255)
     post = models.CharField('Post Category ',max_length=255)
     ptpublished = models.DateField()
    

class Song(models.Model):
     user = models.ManyToManyField(User)
     stitle = models.CharField('Song title',max_length=255)
     sduration = models.IntegerField('Song Duration')
     
def written_by(self):
    return ",".join([str(p) for p in self.user.all()])
    
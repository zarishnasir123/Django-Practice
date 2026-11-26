from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    # today's date is filled in by itself, but another date can be given too
    publish_date = models.DateField(default=timezone.localdate)

    class Meta:
        # newest posts first. Pagination needs a fixed order, or a post could show up on two pages.
        ordering = ['-publish_date', '-id']

    def __str__(self):
        return self.title

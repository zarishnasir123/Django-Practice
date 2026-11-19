from django.db import models

# Create your models here.
# The same three fields as ContactForm, so every submitted form becomes one row.
class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name

from django.db import models
from django.urls import reverse

# Create your models here.

GENRE_CHOICES = [
    ('fiction', 'Fiction'),
    ('non-fiction', 'Non-fiction'),
    ('fantasy', 'Fantasy'),
    ('mystery', 'Mystery'),
    ('romance', 'Romance'),
    ('science', 'Science'),
    ('history', 'History'),
    ('biography', 'Biography'),
    ('self-help', 'Self-help'),
    ('technology', 'Technology'),
]


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    #unique but optional: null (not '') is stored when empty, so many books can have no ISBN
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    #0.00 to 5.00; the reviews will update it later
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    #saved in MEDIA_ROOT/covers/ (needs Pillow); optional
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    #filled in automatically when the book is added
    created_at = models.DateTimeField(auto_now_add=True)
    #changes every time the book is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    #the address of this book's page; CreateView/UpdateView redirect here after saving.
    #needs a url named 'book_detail' that takes the book's pk (path('<int:pk>/', ..., name='book_detail'))
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

from django.db import models
from django.conf import settings
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

#1 to 5 stars; shows as a dropdown in forms
RATING_CHOICES = [
    (1, '1 - Poor'),
    (2, '2 - Fair'),
    (3, '3 - Good'),
    (4, '4 - Very good'),
    (5, '5 - Excellent'),
]


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    #filled in automatically when the book is added
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    #how a book is shown in the admin and in dropdowns
    def __str__(self):
        return self.title

    #the url of this book's own page, e.g. /book/3/
    #used by {{ book.get_absolute_url }} in templates, redirect(book) in views,
    #and the "View on site" button in the admin
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.pk])

    #average of all its review ratings, e.g. 4.5 (None when it has no reviews yet)
    def average_rating(self):
        return self.reviews.aggregate(avg=models.Avg('rating'))['avg']


class Review(models.Model):
    #related_name='reviews': book.reviews.all() gives all reviews of a book
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    #Django's built-in User (the accounts you log in with)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #newest reviews first
        ordering = ['-created_at']
        #a user can review the same book only once
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='one_review_per_user_per_book'),
        ]

    def __str__(self):
        return f'{self.book} - {self.rating} stars by {self.user}'

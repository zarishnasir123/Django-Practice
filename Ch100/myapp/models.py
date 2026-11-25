from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey = many books for one author.
    # related_name='books' lets us go from an author to the books: author.books.all()
    # on_delete=CASCADE: if an author is deleted, his or her books are deleted too.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # the discount is an amount of money taken off the price (not a percent), 0 means no discount
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # ManyToManyField = a book can have many tags, and a tag can be on many books (a novel, a bestseller...).
    # Django makes a third table by itself to hold the pairs (book, tag).
    # related_name='books' lets us go from a tag to its books: tag.books.all()
    # and book.tags.all() goes from a book to its tags.
    # blank=True: a book is allowed to have no tags.
    tags = models.ManyToManyField(Tag, related_name='books', blank=True)

    def __str__(self):
        return self.title

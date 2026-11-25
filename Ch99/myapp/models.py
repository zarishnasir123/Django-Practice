from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

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

    def __str__(self):
        return self.title

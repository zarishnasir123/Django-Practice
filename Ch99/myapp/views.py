from django.db.models.aggregates import Count
from django.db.models import Avg, Max, Min, Q, Sum
from django.http import HttpResponse
from django.utils.html import escape
from .models import Author

# Create your views here.
def home(request):
    #count the number of books each authoer has
    authors = Author.objects.annotate(book_count = Count('books'))
    print(authors)
    print(vars(authors[2]))
    for author in authors:
        print(author.name, author.book_count,)
    return HttpResponse('<h1>Home Page</h1>')


# ---------- more views with related_name ----------
# In models.py the ForeignKey of Book has related_name='books'.
# That name is what we write in an Author query to reach the books of the author:
#   Count('books')          = how many books    Sum('books__price')  = the price of the books added together
#   filter(books__price=..) = a condition on the books of the author
# Without related_name Django would use the default name: book (Count('book'), book_set.all()).

# A small helper, so every view shows its answer in the same way: a heading and one line for each text.
# escape() makes <, > and & safe, so a name with html in it is shown as text.
def show(heading, lines):
    body = '<br>'.join(escape(line) for line in lines)
    return HttpResponse(f'<h1>{escape(heading)}</h1><p>{body}</p>')


# 1. annotate + Count, ordered. The author with the most books comes first.
# '-book_count' = the biggest number first. We can order by a name made by annotate().
def book_count_view(request):
    authors = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')
    lines = [f'{author.name}: {author.book_count} book(s)' for author in authors]
    return show('Number of books of each author', lines)


# 2. filter on the annotated name. Only the authors with more than 1 book.
# book_count__gt=1 works like any other field: gt = greater than.
def many_books_view(request):
    authors = Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=1)
    lines = [f'{author.name}: {author.book_count} books' for author in authors]
    return show('Authors with more than 1 book', lines)


# 3. the authors without any book. Count gives 0 for them (it does not leave them out).
def no_books_view(request):
    authors = Author.objects.annotate(book_count=Count('books')).filter(book_count=0)
    lines = [author.name for author in authors]
    return show('Authors without books', lines)


# 4. more than one annotate in a query: Sum, Avg, Min and Max of the price of the books of each author.
# 'books__price' = the price field of the books of the author (two underscores).
# An author without books gets None for all four, so we check for None first.
# :.2f shows the number with 2 decimals (SQLite adds decimal numbers with extra digits, like 43.9900000000000).
def price_report_view(request):
    authors = Author.objects.annotate(
        total=Sum('books__price'),
        average=Avg('books__price'),
        cheapest=Min('books__price'),
        dearest=Max('books__price'),
    )
    lines = []
    for author in authors:
        if author.total is None:
            lines.append(f'{author.name}: no books')
        else:
            lines.append(f'{author.name}: total {author.total:.2f}, average {author.average:.2f}, cheapest {author.cheapest:.2f}, dearest {author.dearest:.2f}')
    return show('Price report of the books of each author', lines)


# 5. Count with a condition: filter=Q(...) counts only the books that match.
# Here: how many books of each author have a discount (discount greater than 0).
def discount_count_view(request):
    authors = Author.objects.annotate(
        all_books=Count('books'),
        discounted=Count('books', filter=Q(books__discount__gt=0)),
    )
    lines = [f'{author.name}: {author.discounted} of {author.all_books} books have a discount' for author in authors]
    return show('Books with a discount', lines)


# 6. a condition on the related books inside filter(): authors who have a book that costs more than 12.
# One author can match with several books and would come back several times, so distinct() is added.
def expensive_authors_view(request):
    authors = Author.objects.filter(books__price__gt=12).distinct()
    lines = [author.name for author in authors]
    return show('Authors with a book that costs more than 12', lines)


# 7. the other direction: from an author to his or her books, with author.books.all().
# prefetch_related('books') brings all the books in one extra query, so the loop does not ask the database again for every author.
def author_books_view(request):
    authors = Author.objects.prefetch_related('books')
    lines = []
    for author in authors:
        titles = [book.title for book in author.books.all()]
        lines.append(f'{author.name}: ' + (', '.join(titles) if titles else 'no books'))
    return show('Books of each author (author.books.all())', lines)

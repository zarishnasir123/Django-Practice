from django.shortcuts import render
from .models import Book, Author
from django.db import connection, reset_queries

# Create your views here.

# Prints how many queries went to the database, and the SQL of each one.
# connection.queries is a list that Django fills only while DEBUG = True in settings.py.
def show_queries():
    queries = connection.queries
    print('Number of queries:', len(queries))
    for number, query in enumerate(queries, start=1):
        print(number, query['sql'])


# def home(request):
#     # empty the list first, so only the queries of this request are counted
#     reset_queries()

#     # every book. The template also shows book.author.name for each book (see home.html).
#     # without select_related()
#     # books = Book.objects.all()
#     # for book in books:
#     #     print(book.title, book.author.name)
        
#     # with select_related()
#     # select_related('author') joins the author table in the SAME query, so book.author is already loaded
#     # and the loop (and the template) do not ask the database again for every book.
#     books = Book.objects.select_related('author').all()
#     for book in books:
#         print(book.title, book.author.name)
#     # The return must be the LAST line: nothing after it runs.
#     # The books are sent to the template as the context, or the table would be empty.
#     # render() builds the page now, and the template can also ask the database (book.author.name),
#     # so show_queries() is called after render() to count those queries too.
#     response = render(request, 'myapp/home.html', {'books': books})
#     show_queries()
#     return response


def home(request):
    # empty the list first, so only the queries of this request are counted
    reset_queries()
    books = Book.objects.select_related('author').prefetch_related('tags')
    response = render(request, 'myapp/home.html', {'books': books})
    show_queries()
    return response

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, F, Q
from .forms import ReviewForm, BookForm
from .models import Book, Review, GENRE_CHOICES

# Create your views here.

#options for the filter bar on the home page: (value in the url, text shown)
RATING_FILTERS = [
    ('', 'Any rating'),
    ('3', '3 stars & up'),
    ('4', '4 stars & up'),
    ('4.5', '4.5 stars & up'),
]

SORT_OPTIONS = [
    ('title', 'Title (A-Z)'),
    ('rating', 'Highest rated'),
    ('reviews', 'Most reviewed'),
    ('newest', 'Newest added'),
]


#READ: all books, with search, filters and sorting taken from the url, e.g. /?q=clean&genre=technology
def home(request):
    #the database works out each book's average rating and number of reviews,
    #so we can filter and sort by them (and the page doesn't need extra queries)
    books = Book.objects.annotate(avg_rating=Avg('reviews__rating'), review_count=Count('reviews'))

    #values from the filter form (it uses method="get", so they arrive in request.GET)
    q = request.GET.get('q', '').strip()
    genre = request.GET.get('genre', '')
    rating = request.GET.get('rating', '')
    sort = request.GET.get('sort', 'title')

    #ignore values that aren't in our own lists (someone could type anything in the url)
    if genre not in dict(GENRE_CHOICES):
        genre = ''
    if rating not in dict(RATING_FILTERS):
        rating = ''
    if sort not in dict(SORT_OPTIONS):
        sort = 'title'

    #search: title OR author contains the text (icontains ignores capital letters)
    if q:
        books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))

    if genre:
        books = books.filter(genre=genre)

    if rating:
        books = books.filter(avg_rating__gte=float(rating))

    if sort == 'rating':
        #books without reviews go to the end
        books = books.order_by(F('avg_rating').desc(nulls_last=True), 'title')
    elif sort == 'reviews':
        books = books.order_by('-review_count', 'title')
    elif sort == 'newest':
        books = books.order_by('-created_at')
    else:
        books = books.order_by('title')

    return render(request, 'book/home.html', {
        'books': books,
        #the chosen values, so the form keeps showing them
        'q': q,
        'genre': genre,
        'rating': rating,
        'sort': sort,
        #the options for the dropdowns
        'genre_choices': GENRE_CHOICES,
        'rating_filters': RATING_FILTERS,
        'sort_options': SORT_OPTIONS,
        #True when any filter is used: shows the "Clear" link and the "no match" message
        'filtering': bool(q or genre or rating),
    })


#one book with its reviews; pk comes from the url /book/<pk>/
def book_detail(request, pk):
    #404 page instead of a crash when no book has this id
    book = get_object_or_404(Book, pk=pk)

    #has the logged-in user already reviewed this book? (decides which button the page shows)
    user_has_reviewed = request.user.is_authenticated and book.reviews.filter(user=request.user).exists()

    return render(request, 'book/book_detail.html', {
        'book': book,
        'user_has_reviewed': user_has_reviewed,
    })


#write a review; @login_required sends visitors to the login page first
#(and back here after logging in, through ?next=)
@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)

    #one review per user per book
    if book.reviews.filter(user=request.user).exists():
        messages.info(request, 'You have already reviewed this book.')
        return redirect(book)

    if request.method == 'POST':
        #the book and the logged-in user are set here; the form only has rating and comment
        form = ReviewForm(request.POST, instance=Review(book=book, user=request.user))

        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your review has been posted.')
            #redirect(book) uses Book.get_absolute_url() -> /book/<pk>/
            return redirect(book)

    else:
        form = ReviewForm()

    return render(request, 'book/review_form.html', {
        'book': book,
        'form': form,
    })


# ===== Book CRUD (Create, Update, Delete); Read is home + book_detail above =====
# only staff users (like root) can add, edit or delete books; readers write reviews

#CREATE: add a new book
@login_required
def add_book(request):
    if not request.user.is_staff:
        messages.error(request, 'Only staff members can add books.')
        return redirect('home')

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save()
            messages.success(request, f'"{book.title}" has been added.')
            return redirect(book)

    else:
        form = BookForm()

    return render(request, 'book/book_form.html', {
        'form': form,
        'heading': 'Add a book',
    })


#UPDATE: edit an existing book; instance=book fills the form with its current values
@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if not request.user.is_staff:
        messages.error(request, 'Only staff members can edit books.')
        return redirect(book)

    #keep the saved title for the heading (an invalid form can change book.title in memory)
    original_title = book.title

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, f'"{book.title}" has been updated.')
            return redirect(book)

    else:
        form = BookForm(instance=book)

    return render(request, 'book/book_form.html', {
        'form': form,
        'book': book,
        'heading': f'Edit "{original_title}"',
        'original_title': original_title,
    })


#DELETE: GET shows a confirmation page, POST really deletes
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if not request.user.is_staff:
        messages.error(request, 'Only staff members can delete books.')
        return redirect(book)

    if request.method == 'POST':
        title = book.title
        #its reviews are deleted too (on_delete=models.CASCADE in Review.book)
        book.delete()
        messages.warning(request, f'"{title}" has been deleted.')
        return redirect('home')

    return render(request, 'book/book_confirm_delete.html', {'book': book})

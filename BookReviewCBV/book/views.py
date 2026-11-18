from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from .forms import BookForm
from .models import Book, GENRE_CHOICES

# Create your views here.
# Class based views. The plain View class has no get_context_data(), so these use TemplateView:
#  - get() is already written: it calls get_context_data() and renders template_name
#  - get_context_data() collects everything the template needs (the book, the form, the list...)
#  - post() (only where there is a form or a button) does the work, then redirects or shows the form again


#all books, with filters read from the address: /?q=code&genre=technology&min_rating=4&sort=-average_rating
class BookListView(TemplateView):
    template_name = 'book/book_list.html'

    #what each sort option means: the value in the address -> the field to order by
    SORTS = {
        'title': 'title',
        'author': 'author',
        '-average_rating': '-average_rating',
        '-publication_date': '-publication_date',
        '-created_at': '-created_at',
    }
    SORT_CHOICES = [
        ('title', 'Title (A-Z)'),
        ('author', 'Author (A-Z)'),
        ('-average_rating', 'Highest rated'),
        ('-publication_date', 'Newest published'),
        ('-created_at', 'Recently added'),
    ]
    RATING_CHOICES = [('', 'Any rating'), ('3', '3+ stars'), ('4', '4+ stars'), ('4.5', '4.5+ stars')]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        params = self.request.GET

        q = params.get('q', '').strip()
        genre = params.get('genre', '')
        min_rating = params.get('min_rating', '')
        sort = params.get('sort', 'title')

        books = Book.objects.all()

        #search: the text is in the title OR in the author (a Q object joins them with |)
        if q:
            books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))

        #only genres and ratings from our own lists are used, so a changed address can't break the query
        if genre not in dict(GENRE_CHOICES):
            genre = ''
        if min_rating not in ('3', '4', '4.5'):
            min_rating = ''

        if genre:
            books = books.filter(genre=genre)
        if min_rating:
            books = books.filter(average_rating__gte=min_rating)

        books = books.order_by(self.SORTS.get(sort, 'title'))

        context['book_list'] = books

        #the chosen values go back to the template, so the filter bar keeps showing them
        context.update({
            'q': q,
            'genre': genre,
            'min_rating': min_rating,
            'sort': sort,
            'genre_choices': GENRE_CHOICES,
            'rating_choices': self.RATING_CHOICES,
            'sort_choices': self.SORT_CHOICES,
            'filtered': bool(q or genre or min_rating),
        })

        #session: the ids of the last books this visitor opened (saved by BookDetailView)
        recent_ids = self.request.session.get('recent_books', [])
        books_by_id = Book.objects.in_bulk(recent_ids)
        #keep the order of the ids; a book that was deleted since is skipped
        context['recent_books'] = [books_by_id[pk] for pk in recent_ids if pk in books_by_id]
        return context


#one book; pk comes from the url: path('<int:pk>/') and arrives in kwargs
class BookDetailView(TemplateView):
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context['book'] = book

        #session: remember this book as the most recent one (keep only the last 5, no repeats)
        recent = self.request.session.get('recent_books', [])
        if book.pk in recent:
            recent.remove(book.pk)
        recent.insert(0, book.pk)
        self.request.session['recent_books'] = recent[:5]
        return context


#add a book
class BookCreateView(TemplateView):
    template_name = 'book/book_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #post() passes the form it already checked (with its errors); on a GET there is none yet
        if 'form' not in context:
            context['form'] = BookForm()
        return context

    def post(self, request, *args, **kwargs):
        #request.FILES holds the uploaded cover image
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            #the message is kept in the session and shown once, on the next page
            messages.success(request, f'"{book.title}" was added.')
            #redirect(book) goes to book.get_absolute_url(), the book_detail page
            return redirect(book)
        messages.error(request, 'Please correct the errors below.')
        return self.render_to_response(self.get_context_data(form=form))


#edit a book: the same form, filled with the book's current values (instance=book)
class BookUpdateView(TemplateView):
    template_name = 'book/book_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context['object'] = book
        if 'form' not in context:
            context['form'] = BookForm(instance=book)
        return context

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{book.title}" was updated.')
            return redirect(book)
        messages.error(request, 'Please correct the errors below.')
        return self.render_to_response(self.get_context_data(form=form, **kwargs))


#delete a book: get() asks "are you sure?", post() (the button on that page) really deletes
class BookDeleteView(TemplateView):
    template_name = 'book/book_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        title = book.title
        #deleting the row does not delete the image file, so remove it first
        book.cover_image.delete(save=False)
        book.delete()
        messages.success(request, f'"{title}" was deleted.')
        return redirect('book_list')


#-------- redirect views: they have no page of their own, they send the visitor to another address --------

#/latest/ goes to the book that was added last
class LatestBookRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        book = Book.objects.order_by('-created_at').first()
        if book:
            return book.get_absolute_url()
        return reverse('book_list')   #no books yet


#/random/ goes to a different book every time
class RandomBookRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        book = Book.objects.order_by('?').first()
        if book:
            return book.get_absolute_url()
        return reverse('book_list')

from django import forms
from .models import Book, Review

# class="field" is the Tailwind input style defined in z_dev/input.css


#write a review: only rating and comment are typed in;
#the view sets the book and the logged-in user, e.g.
#    form = ReviewForm(request.POST, instance=Review(book=book, user=request.user))
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'comment': 'Your review',
        }
        widgets = {
            'rating': forms.Select(attrs={'class': 'field'}),
            'comment': forms.Textarea(attrs={'class': 'field', 'rows': 4, 'placeholder': 'What did you think of this book?'}),
        }

    #book and user are not form fields, so the ModelForm skips the model's
    #"one review per user per book" rule; check it here so a second review
    #shows a form error instead of crashing with an IntegrityError
    def clean(self):
        cleaned_data = super().clean()
        review = self.instance

        if review.book_id and review.user_id and not review.pk:
            if Review.objects.filter(book_id=review.book_id, user_id=review.user_id).exists():
                raise forms.ValidationError('You have already reviewed this book.')

        return cleaned_data


#add a book from the site (the admin can still add books too)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_year', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Book title'}),
            'author': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Author name'}),
            'genre': forms.Select(attrs={'class': 'field'}),
            'published_year': forms.NumberInput(attrs={'class': 'field', 'placeholder': 'e.g. 2018'}),
            'description': forms.Textarea(attrs={'class': 'field', 'rows': 4, 'placeholder': 'Short description (optional)'}),
        }

from django import forms
from .models import Book


#average_rating, created_at and updated_at are not typed in:
#the rating comes from the reviews and the two dates are set automatically
#Bootstrap classes: form-control for inputs and textareas, form-select for dropdowns
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'isbn', 'publication_date', 'published_year', 'cover_image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '13 digits (optional)'}),
            #type="date" shows a date picker in the browser
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'published_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2008'}),
            #FileInput (not the default clearable one) fits Bootstrap; leaving it empty keeps the old cover
            'cover_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    #after checking, give every field that has an error Bootstrap's is-invalid class (red border)
    def is_valid(self):
        valid = super().is_valid()
        for name in self.errors:
            if name in self.fields:
                self.fields[name].widget.attrs['class'] += ' is-invalid'
        return valid

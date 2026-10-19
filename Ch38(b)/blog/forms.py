from django import forms
from .models import Post


#content is a CKEditor5Field in the model, so it gets the CKEditor 5 editor automatically
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        #'field' is the Tailwind input style from z_dev/input.css
        #(content keeps CKEditor's own widget; its JavaScript looks for that textarea)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Post title'}),
        }

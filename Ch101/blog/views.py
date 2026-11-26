from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()                      # newest first (ordering in models.py)

    paginator = Paginator(posts, per_page=5)                 # cut the posts into pages of 5
    page_number = request.GET.get('page')           # the ?page=2 part of the url (None if there is none)
    # get_page() gives the posts of that page. It never crashes:
    # no number or a text like abc gives page 1, and a number that does not exist (999 or 0) gives the last page.
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'page_obj': page_obj})

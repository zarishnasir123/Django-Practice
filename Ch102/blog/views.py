from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post

# Create your views here.
# The same page as Ch101, with a class based view. ListView does the pagination by itself.
class PostListView(ListView):
    model = Post                          # all the posts, newest first (ordering in models.py)
    template_name = 'blog/home.html'      # without it Django would look for blog/post_list.html
    context_object_name = 'posts'         # the name of the posts of the page in the template
    paginate_by = 7                       # this one line makes pages of 7
    # orphans: if the last page would have this many posts or fewer, they join the page before it.
    # 45 posts in pages of 7 leaves 3 over, so we get 6 pages (the last one has 10), not 7.
    paginate_orphans = 3

    # With paginate_by the template also gets:
    #   page_obj      the current page (number, has_next, has_previous...)
    #   paginator     all the pages (count, num_pages, page_range)
    #   is_paginated  True when there is more than one page
    # A wrong page like ?page=999 or ?page=abc gives a 404 page. ?page=last gives the last page.


# The same page WITHOUT ListView: a plain View class, and we use the Paginator by hand.
# Everything that ListView did for us is written here. It uses the same template.
class PostPaginatorView(View):
    # class attributes, like in ListView, so they are easy to change
    paginate_by = 7
    paginate_orphans = 3

    def get(self, request):
        posts = Post.objects.all()                       # newest first (ordering in models.py)

        # cut the posts into pages
        paginator = Paginator(posts, self.paginate_by, orphans=self.paginate_orphans)

        page_number = request.GET.get('page')            # the ?page=2 part of the url
        # get_page() never crashes: a text like abc gives page 1, a number that does not exist gives the last page
        page_obj = paginator.get_page(page_number)

        # the same names that ListView sends, so home.html works without any change
        context = {
            'posts': page_obj,                           # the posts of this page
            'page_obj': page_obj,
            'paginator': paginator,
            'is_paginated': page_obj.has_other_pages(),  # True when there is more than one page
        }
        return render(request, 'blog/home.html', context)

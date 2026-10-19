from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = PostForm()

    #newest posts first
    posts = Post.objects.order_by('-id')

    return render(request, 'blog/home.html', {
        'form': form,
        'posts': posts
    })

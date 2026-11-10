from django.shortcuts import render
from .models import Page, Post, Song
from django.contrib.auth.models import User

# Create your views here.
# Filters can follow a relationship with two underscores: field__relatedfield=value
# Uncomment ONE line at a time in each view to try it.
def home(request):
    return render(request, 'myapp/home.html')


#-------- starting from User, going to the related model --------
#lowercase model name = the reverse link (page, post, song)
def show_user_data(request):
    data1 = User.objects.all()

    #users whose page is in this category (one to one, reverse)
    data2 = User.objects.filter(page__pcat='tech')

    #users who wrote a post with this title (many to one, reverse)
    # data2 = User.objects.filter(post__title='Django Basics')

    #users who have at least one post; distinct() removes repeats (zarish has two posts)
    # data2 = User.objects.filter(post__isnull=False).distinct()

    #users linked to this song (many to many, reverse)
    # data2 = User.objects.filter(song__stitle='Pasoori')

    #users who have no page
    # data2 = User.objects.filter(page__isnull=True)

    return render(request, 'myapp/user.html', {'data1': data1, 'data2': data2})


#-------- one to one: Page -> User --------
def show_page_data(request):
    data2 = Page.objects.all()

    #the page of one user
    # data2 = Page.objects.filter(user__username='zarish')

    #pages whose user's first name starts with N
    # data2 = Page.objects.filter(user__first_name__startswith='N')

    #pages of normal (non-admin) users only
    # data2 = Page.objects.filter(user__is_superuser=False)

    #category contains "tech", ignoring capitals
    # data2 = Page.objects.filter(pcat__icontains='tech')

    return render(request, 'myapp/page.html', {'data2': data2})


#-------- many to one: Post -> User --------
def show_post_data(request):
    data3 = Post.objects.all()

    #every post of one user (zarish has two)
    # data3 = Post.objects.filter(user__username='zarish')

    #posts by users whose email ends with example.com
    # data3 = Post.objects.filter(user__email__endswith='example.com')

    #posts published after a date, newest first
    # data3 = Post.objects.filter(ptpublished__gt='2025-02-03').order_by('-ptpublished')

    #posts whose user has a page in this category (Post -> User -> Page)
    # data3 = Post.objects.filter(user__page__pcat='Education')

    return render(request, 'myapp/post.html', {'data3': data3})


#-------- many to many: Song <-> User --------
def show_song_data(request):
    data4 = Song.objects.all()

    #songs linked to one user
    # data4 = Song.objects.filter(user__username='zarish')

    #songs linked to any of these users; distinct() because one song can match twice
    # data4 = Song.objects.filter(user__username__in=['noor', 'sami']).distinct()

    #songs longer than 4 minutes
    # data4 = Song.objects.filter(sduration__gt=240)

    #songs that have no users at all
    # data4 = Song.objects.filter(user__isnull=True)

    return render(request, 'myapp/song.html', {'data4': data4})

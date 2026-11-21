from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View

# Create your views here.
# function based views
def homeview(request):
    url = reverse('home')
    print(url)
    return HttpResponse('<h1>Home (function based view)</h1>')


def productview(request, pk):
    url = reverse('product', kwargs={'pk':pk})
    print(url)
    return HttpResponse('<h1>Products (function based view)</h1>')


# a class based view
class AboutView(View):
    def get(self, request):
        url = reverse_lazy('about')
        print(url)
        return HttpResponse('<h1>About (class based view)</h1>')


class PostView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        url = reverse_lazy('post', kwargs={'pk':pk})
        print(url)
        return HttpResponse("<h1>Post Page class based </h1>")
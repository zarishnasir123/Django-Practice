from django.urls import reverse
from django.views.generic import RedirectView, TemplateView

# Create your views here.
# RedirectView only has a get(): it sends the browser to another address (302 or 301).
# It needs ONE of:  url = '/some/path/'   or   pattern_name = 'url_name'

#-------- normal pages the redirects point to --------

class HomeView(TemplateView):
    template_name = 'myapp/home.html'


class AboutView(TemplateView):
    template_name = 'myapp/about.html'


class NewsView(TemplateView):
    template_name = 'myapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = kwargs['id']
        return context


class ResultsView(TemplateView):
    template_name = 'myapp/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


#-------- redirect views --------

#a redirect class of your own: get_redirect_url() decides where to go
#(it gets the same kwargs as the URL, so path('old-news/<int:id>/') gives kwargs['id'])
class OldNewsRedirectView(RedirectView):
    pattern_name = 'news'      #the URL name to go to; kwargs are passed on to it
    permanent = False          #False = 302 (temporary), True = 301 (permanent)

    def get_redirect_url(self, *args, **kwargs):
        print('Redirecting old news', kwargs['id'])
        return super().get_redirect_url(*args, **kwargs)


#always send visitors to the newest news (here the id is fixed to 99)
class LatestNewsRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        newest_id = 99
        return reverse('news', kwargs={'id': newest_id})

from django.shortcuts import render
from django.views import View
from .forms import ContactForm

# Create your views here.

#-------- function based views (FBV) --------

# def home(request):
#     return render(request, 'myapp/home.html')

# def about(request):
#     return render(request, 'myapp/about.html', {'msg': 'Welcome to the about page'})

# #one view, two templates: the form on GET, the thank you page after a valid POST
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return render(request, 'myapp/thankyou.html', {
#                 'name': form.cleaned_data['name'],
#                 'email': form.cleaned_data['email'],
#             })
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# #one view for both news pages: urls.py says which template to use
# def news(request, template_name):
#     template = f'myapp/{template_name}'
#     return render(request, template, {'info': 'Django 6.1 released'})


#-------- class based views (CBV) with the base View class --------
# A class view has one method per HTTP method: get() for GET, post() for POST.
# In urls.py it is connected with .as_view(), which turns the class into a view function.

class HomeView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'myapp/about.html', {'msg': 'Welcome to the about page'})


#no "if request.method == 'POST'": Django calls get() or post() by itself
class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'myapp/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'myapp/thankyou.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
            })
        return render(request, 'myapp/contact.html', {'form': form})


#template_name is a class attribute; urls.py can change it with .as_view(template_name=...)
class NewsView(View):
    template_name = 'myapp/news.html'

    def get(self, request):
        return render(request, self.template_name, {'info': 'Django 6.1 released'})

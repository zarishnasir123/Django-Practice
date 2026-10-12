from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'core/home.html')

def about(req):
    return render(req, 'core/about.html')

from django.shortcuts import render

# Create your views here.
def learn_django(req):
    return render(req, 'course/django.html')

def learn_python(req):
    return render(req, 'course/python.html')
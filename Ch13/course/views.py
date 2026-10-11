from django.shortcuts import render

# Create your views here.
def learn_django(req):
    return render(req, 'course/django.html', {'nm': 'Django 5'})
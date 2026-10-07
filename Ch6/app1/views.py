from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LearnDjango(request):
    return HttpResponse("Hello Django")

def Home(request):
    return HttpResponse("Home Page")

def learn_python(request):
    return HttpResponse('<h1>Hello python</h1>')

def math(request):
    a = 10 + 10
    return HttpResponse(f'The sum of 10 and 10 is {a}')
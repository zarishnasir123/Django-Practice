from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(req, **kawrgs):
    status = kawrgs.get('status', 'not allowed')
    return HttpResponse(f'<h1>Hello django App1{status}</h1>')

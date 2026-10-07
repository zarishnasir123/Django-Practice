from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2(request):
    return HttpResponse("App2 page")

def app2home(request):
    return HttpResponse("App2 Home Page")

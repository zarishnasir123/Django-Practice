from django.http import HttpResponse
from django.shortcuts import render
from blog import signals

# Create your views here.
def home(req):
    signals.notification.send(sender=None, req=req, user=["zarish", "nasir"])
    return HttpResponse("this is home page")
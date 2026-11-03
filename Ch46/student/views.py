from django.shortcuts import render
from datetime import datetime, timedelta, timezone

# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('newtoken', 'y111111', max_age=3600)
    # response.set_cookie(
    #     'newtoken', 'y111111',
    #     expires=datetime.now (timezone.utc) + timedelta(days=2))
    return response

def getcookie(request):
    newtoken = request.COOKIES.get('newtoken', 'defaulttoken123')
    response = render(request, 'student/getcookie.html', {'newtoken' : newtoken})
    return response
    
def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('newtoken')
    return response

def setsignedcookie(request):
    response = render(request, 'student/setsignedcookie.html')
    response.set_signed_cookie('token', 't123456', salt='tk')
    return response

def getsignedcookie(request):
    token = request.get_signed_cookie('token', default='guesttoken', salt= 'tk')
    response = render(request, 'student/getsignedcookie.html', {'token' : token})
    return response
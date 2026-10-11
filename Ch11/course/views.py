from django.shortcuts import render

# Create your views here.
def learn_django(req):
    coursename = {'cname': 'Django 5.2'}
    return render(req, 'course/django.html', context=coursename)  
    # return render(req, 'course/django.html',  {'cname': 'Django 5.0'})
    # return render(req, 'course/django.html', coursename)
    

def learn_fasiapi(req):
    seats = 10
    coursename = {
        'cname' : 'FastApi',
        'version' : '3.0',
        'st' : seats
    }
    
    return render(req, 'course/fastapi.html', context=coursename)
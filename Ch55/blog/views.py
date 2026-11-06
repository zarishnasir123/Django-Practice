from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('i am home view')
    return render(request, 'blog/home.html')

def math(request):
    print("i am my math view")
    a= 10/0
    return render(request, 'blog/math.html', {'a' : a})

def user(request):
    print("i am user info view")
    context = {'name': 'zarish'}
    return TemplateResponse(request, 'blog/user.html', context)

def uc(request):
    return render(request, 'blog/uc.html')
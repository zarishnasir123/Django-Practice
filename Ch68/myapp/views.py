from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'cart_items':3}
    return render(request, 'myapp/home.html', context)

def product(request):
    context = {'cart_items':3}
    return render(request, 'myapp/product.html', context)

def contact(request):
    context = {'cart_items':3}
    return render(request, 'myapp/contact.html', context)

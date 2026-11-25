from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import Product

# Create your views here.
# HttpResponse sends text/html. JsonResponse sends JSON, so another program (or JavaScript) can read it easily.
# def homeview(request):
#     return HttpResponse('<h1>Home Page</h1>')

# ---------- function based views ----------

# 1. JsonResponse with a dictionary
# JsonResponse turns the python dictionary into JSON text,
# and it also sets the header Content-Type: application/json for us.
def homeview(request):
    data = {
        'msg' : 'hello home page',
        'status' : 'success'
    }
    return JsonResponse(data)


# 2. data from the database
# values() gives every row as a dictionary, but it is still a QuerySet, not a list.
# JSON can't hold a QuerySet, so list() is used to change it into a normal python list.
# The list is put inside a dictionary, so the answer has a name for it ('products').
def productlistview(request):
    products = list(Product.objects.values('id', 'name', 'price'))
    data = {
        'count' : len(products),
        'products' : products
    }
    return JsonResponse(data)


# 3. safe=False
# By default JsonResponse only accepts a dictionary, and a list gives TypeError.
# safe=False tells Django "yes, I know, I want to send a list".
def productnamesview(request):
    names = list(Product.objects.values_list('name', flat=True))
    return JsonResponse(names, safe=False)


# 4. one row with the pk from the url, and an error in JSON
# filter(pk=pk).first() gives the product, or None if there is no product with that pk (get() would crash instead).
# If it is None, we send an error message with status=404.
# (status is the number the browser sees: 200 = ok, 404 = not found)
def productdetailview(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product is None:
        return JsonResponse({'error' : 'Product not found'}, status=404)

    data = {
        'id' : product.id,
        'name' : product.name,
        'price' : product.price,   # price is a Decimal, JsonResponse sends it as text, like "899.99"
    }
    return JsonResponse(data)


# 5. status code, header and pretty printing
# status=201 means "created" (the usual number after something new is made).
# A response works like a dictionary, so response['name'] = value adds a header.
# json_dumps_params={'indent': 4} writes the JSON in lines so it is easy to read in the browser.
def createdview(request):
    response = JsonResponse(
        {'msg' : 'product created', 'status' : 'success'},
        status=201,
        json_dumps_params={'indent' : 4},
    )
    response['X-Student-Note'] = 'learning JsonResponse'
    return response


# ---------- class based views ----------
# The same two pages again as classes. The view has a get() method, and it returns a JsonResponse too.

class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values('id', 'name', 'price'))
        return JsonResponse({'count' : len(products), 'products' : products})


class ProductDetailView(View):
    # the pk from the url comes in as an argument of get()
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if product is None:
            return JsonResponse({'error' : 'Product not found'}, status=404)
        return JsonResponse({'id' : product.id, 'name' : product.name, 'price' : product.price})

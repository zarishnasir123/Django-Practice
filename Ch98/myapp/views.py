import json
from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.views import View
from django.http import HttpResponse, JsonResponse


# Create your views here.
# The home page shows the empty form. The list and the buttons will be filled by JavaScript (AJAX) later.
def home(request):
    form = ProductForm()
    return render(request, 'myapp/home.html', {'form': form})


# One product as a dictionary, so it can be sent as JSON
def product_to_dict(product):
    return {'id': product.id, 'name': product.name, 'price': product.price}


# The errors of a form as a dictionary, like {'name': ['This field is required.']}
def form_errors(form):
    return {field: list(messages) for field, messages in form.errors.items()}


# The API for all the products: the url is api/products/
# GET = read the list, POST = create a new product
class ProductAPI(View):
    # READ: send all the products
    def get(self, request):
        products = list(Product.objects.values('id', 'name', 'price'))
        return JsonResponse(products, safe=False)

    # CREATE: the page sends the new product as JSON text in request.body
    def post(self, request):
        data = json.loads(request.body)      # JSON text -> python dictionary
        form = ProductForm(data)             # the same form, so the same validation (forms.py)
        if form.is_valid():
            product = form.save()
            return JsonResponse(product_to_dict(product), status=201)   # 201 = created
        return JsonResponse({'errors': form_errors(form)}, status=400)  # 400 = the data is wrong


# The API for one product: the url is api/products/<pk>/
# GET = read one, PUT = update, DELETE = delete
class ProductDetailAPI(View):
    # READ one product
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if product is None:
            return JsonResponse({'error': 'Product not found'}, status=404)
        return JsonResponse(product_to_dict(product))

    # UPDATE: the same form again, but with instance=product, so it changes this product and does not make a new one
    def put(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if product is None:
            return JsonResponse({'error': 'Product not found'}, status=404)

        data = json.loads(request.body)
        form = ProductForm(data, instance=product)
        if form.is_valid():
            product = form.save()
            return JsonResponse(product_to_dict(product))
        return JsonResponse({'errors': form_errors(form)}, status=400)

    # DELETE
    def delete(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if product is None:
            return JsonResponse({'error': 'Product not found'}, status=404)

        product.delete()
        return JsonResponse({'msg': 'Product deleted'})

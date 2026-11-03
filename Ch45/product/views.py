from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.
# each view needs its own permission (set in core/permission_config.py)
# @login_required sends visitors to log in first; raise_exception gives logged-in users without the permission a 403 page


#READ: every product
@login_required
@permission_required('product.view_product', raise_exception=True)
def product_list(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'product/product_list.html', {'products': products})


#CREATE
@login_required
@permission_required('product.add_product', raise_exception=True)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'"{product.name}" has been added.')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product/product_form.html', {'form': form, 'heading': 'Add product'})


#UPDATE: instance=product fills the form with its current values
@login_required
@permission_required('product.change_product', raise_exception=True)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{product.name}" has been updated.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/product_form.html', {'form': form, 'heading': 'Edit product', 'product': product})


#DELETE: GET asks first, POST really deletes
@login_required
@permission_required('product.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f'"{name}" has been deleted.')
        return redirect('product_list')

    return render(request, 'product/product_confirm_delete.html', {'product': product})

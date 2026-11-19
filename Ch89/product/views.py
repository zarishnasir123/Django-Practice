from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, ListView
from .models import Product

# Create your views here.
# The shop window: every product, from every seller, read only.
#
# PermissionRequiredMixin is the second way to restrict a page (the first was the role mixins of Ch88):
# it does not ask "is this user a customer?", it asks "may this user do view_product?".
# The answer comes from has_perms() in accounts/models.py. A visitor who is not logged in goes to the
# login page, a logged in user without the permission gets the 403 page.
class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'product.view_product'
    queryset = Product.objects.select_related('seller')   # select_related: one query, the seller comes with each product
    ordering = ['name']
    # model Product + this app = the template product/product_list.html and the name product_list


class ProductDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'product.view_product'
    queryset = Product.objects.select_related('seller')
    # the template is product/product_detail.html, the product arrives as "product" (and "object")

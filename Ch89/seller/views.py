from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from accounts.forms import SignUpForm
from accounts.mixins import SellerRequiredMixin
from product.models import Product
from .forms import ProductForm

# Create your views here.
class SellerSignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'Seller'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_seller = True
        user.save()
        return redirect('login')


# The seller's page. Only a logged in seller can open it (a visitor goes to the login page,
# a customer gets a 403 page). This one still uses the role mixin of Ch88.
class SellerDashboardView(SellerRequiredMixin, TemplateView):
    template_name = 'seller/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.request.user.products.count()   # products of this seller only
        return context


# ---------- the seller's products: CRUD with generic views ----------
# These pages are restricted with PermissionRequiredMixin (the permission-based way): the seller has
# add_product, change_product and delete_product, a customer does not, so a customer gets the 403 page.
# A seller must also only touch THEIR products, so every queryset is filtered with seller=request.user.
# The templates are named here because the default name (product/product_list.html) belongs to the shop window.

# Read: the products of this seller
class SellerProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'product.change_product'
    template_name = 'seller/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user).order_by('-created_at')


# Create: the seller is set here, from the logged in user
class SellerProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'product.add_product'
    form_class = ProductForm
    template_name = 'seller/product_form.html'
    success_url = reverse_lazy('seller_products')

    def form_valid(self, form):
        form.instance.seller = self.request.user   # form.instance = the Product being saved
        return super().form_valid(form)


# Update: another seller's product is not in the queryset, so it gives a 404
class SellerProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'product.change_product'
    form_class = ProductForm
    template_name = 'seller/product_form.html'
    success_url = reverse_lazy('seller_products')

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)


# Delete: GET asks "are you sure?", a POST deletes
class SellerProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'product.delete_product'
    template_name = 'seller/product_confirm_delete.html'
    success_url = reverse_lazy('seller_products')

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)

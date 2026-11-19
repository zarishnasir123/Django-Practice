from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from accounts.forms import SignUpForm

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


# The seller's page
class SellerDashboardView(TemplateView):
    template_name = 'seller/dashboard.html'

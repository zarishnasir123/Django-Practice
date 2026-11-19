from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView, TemplateView
from accounts.decorators import anonymous_required, seller_required
from accounts.forms import SignUpForm

# Create your views here.
@method_decorator(anonymous_required, name='dispatch')
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


# The seller's page. Several decorators can also be given as a list, in one method_decorator.
# The list is used in the order it is written, the same as stacking them one under the other:
# never_cache is the outer one, seller_required the inner one.
@method_decorator([never_cache, seller_required], name='dispatch')
class SellerDashboardView(TemplateView):
    template_name = 'seller/dashboard.html'

from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView, TemplateView
from accounts.decorators import anonymous_required, customer_required
from accounts.forms import SignUpForm

# Create your views here.
# method_decorator(decorator, name='dispatch') on the class:
#  - dispatch() is the method every request goes through first, it then calls get() or post(),
#    so decorating dispatch protects all the methods of the class at once
#  - name='dispatch' means "put the decorator on the method called dispatch"

# CreateView shows the sign up form and saves it. form_valid() is changed only to mark the new user
# as a customer before saving, and then the visitor goes to the login page.
# anonymous_required: a user who is already logged in is sent to the home page, for GET and POST.
@method_decorator(anonymous_required, name='dispatch')
class CustomerSignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'Customer'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)   # commit=False: the user is made but not saved yet
        user.is_customer = True
        user.save()
        return redirect('login')


# The customer's page, with two decorators stacked on top of each other.
# The one nearest to the class is added first: customer_required runs on the request first
# (a visitor goes to the login page, a seller gets the 403 page), never_cache then marks the answer.
@method_decorator(never_cache, name='dispatch')
@method_decorator(customer_required, name='dispatch')
class CustomerDashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

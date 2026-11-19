from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from accounts.forms import SignUpForm

# Create your views here.
# CreateView shows the sign up form and saves it. form_valid() is changed only to mark the new user
# as a customer before saving, and then the visitor goes to the login page.
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


# The customer's page
class CustomerDashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

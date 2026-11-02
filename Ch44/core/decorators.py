from functools import wraps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


#the dashboard that matches the user's own role (home if they have no role)
def own_dashboard(user):
    if user.is_customer:
        return 'customer_dashboard'
    if user.is_seller:
        return 'seller_dashboard'
    return 'home'


#common check for any role, e.g. role_required('is_seller')
def role_required(role, message):
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapper(request, *args, **kwargs):
            #getattr reads the field by its name: request.user.is_seller
            if not getattr(request.user, role):
                messages.error(request, message)
                return redirect(own_dashboard(request.user))
            return view(request, *args, **kwargs)
        return wrapper
    return decorator


#ready-made decorators for the two roles
customer_required = role_required('is_customer', 'This page is only for customers.')
#sellers also need an admin's approval, so one check isn't enough
def seller_required(view):
    @wraps(view)
    @role_required('is_seller', 'This page is only for sellers.')
    def wrapper(request, *args, **kwargs):
        if not request.user.is_seller_approved:
            messages.error(request, 'Your seller account is waiting for admin approval.')
            return redirect('home')
        return view(request, *args, **kwargs)
    return wrapper

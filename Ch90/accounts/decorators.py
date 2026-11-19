from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


# A decorator is a function that takes a view and gives back a new view that checks something first.
# These are plain function decorators, like the ones I wrote in Ch43. They are written for ONE request:
#   wrapper(request, ...) runs first; it either stops the request or calls the real view.
# The class based views use them through method_decorator (see customer/views.py).

# only a logged in customer
def customer_required(view_func):
    @wraps(view_func)                     # keeps the name and docstring of the real view
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())   # to the login page, with ?next=
        if not request.user.is_customer:
            raise PermissionDenied                                # the 403 page
        return view_func(request, *args, **kwargs)
    return wrapper


# only a logged in seller
def seller_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not request.user.is_seller:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper


# only a visitor who is NOT logged in (the sign up pages make no sense for a member)
def anonymous_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper

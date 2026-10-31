from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def dashboard_view(request):
    #the other role can't open this page
    if not request.user.is_seller:
        messages.error(request, 'This page is only for sellers.')
        return redirect('customer_dashboard')

    return render(request, 'seller/dashboard.html')

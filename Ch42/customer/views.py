from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def dashboard_view(request):
    #the other role can't open this page
    if not request.user.is_customer:
        messages.error(request, 'This page is only for customers.')
        return redirect('seller_dashboard')

    return render(request, 'customer/dashboard.html')

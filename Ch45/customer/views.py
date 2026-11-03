from django.shortcuts import render
from core.decorators import customer_required

# Create your views here.

@customer_required
def dashboard_view(request):
    return render(request, 'customer/dashboard.html')

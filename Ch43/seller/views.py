from django.shortcuts import render
from core.decorators import seller_required

# Create your views here.

@seller_required
def dashboard_view(request):
    return render(request, 'seller/dashboard.html')

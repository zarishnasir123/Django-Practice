from django.shortcuts import render

# Create your views here.
def fee_courses(req):
    return render(req, 'fees/fee.html')
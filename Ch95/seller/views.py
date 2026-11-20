from django.views.generic import TemplateView

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'seller/dashboard.html'

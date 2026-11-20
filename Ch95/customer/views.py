from django.views.generic import TemplateView

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'


class ProfileView(TemplateView):
    template_name = 'customer/profile.html'

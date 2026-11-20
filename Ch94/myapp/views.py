from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.
# None of these views check the login. The middleware does it for all of them (myapp/middleware.py).
class HomeView(TemplateView):
    template_name = 'myapp/home.html'


class DashboardView(TemplateView):
    template_name = 'myapp/dashboard.html'


# open to everyone: @login_not_required tells the middleware not to ask for a login on this view.
# On a class it goes on dispatch with method_decorator, the same as the decorators of Ch90.
# (Django's own LoginView, LogoutView and the password reset views already have it, so login stays reachable.)
@method_decorator(login_not_required, name='dispatch')
class PublicView(TemplateView):
    template_name = 'myapp/public.html'

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# A mixin is a small class that is written BEFORE the view to add a rule to it:
#   class CustomerDashboardView(CustomerRequiredMixin, TemplateView)
#
# LoginRequiredMixin: a visitor who is not logged in is sent to the login page (LOGIN_URL in settings).
# UserPassesTestMixin: test_func() must return True. If it returns False, a logged in user gets a
# 403 Forbidden page (templates/403.html).
# The order matters: LoginRequiredMixin comes first, so the login is checked before the role.
class CustomerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_customer


class SellerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_seller

from django.contrib.auth.views import redirect_to_login


# A class middleware that makes EVERY page need a login, so no view needs @login_required or LoginRequiredMixin.
# The pages that must stay open are marked with the @login_not_required decorator (see views.py).
# It must be below AuthenticationMiddleware in MIDDLEWARE, because it reads request.user.
class LoginRequiredMiddleware:
    # runs once, when the server starts
    def __init__(self, get_response):
        self.get_response = get_response

    # runs for every request, and only passes it on (the login check is in process_view below)
    def __call__(self, request):
        return self.get_response(request)

    # Django calls this after it has found the view, just before the view runs.
    # That is why the middleware can read what the view says about itself (view_func).
    # Returning None means "go on to the view", returning a response means "stop here and send this".
    def process_view(self, request, view_func, view_args, view_kwargs):
        # @login_not_required sets view_func.login_required = False. A view without it has no such
        # attribute, so getattr gives True: it needs a login.
        if not getattr(view_func, 'login_required', True):
            return None

        if request.user.is_authenticated:
            return None

        # send the visitor to LOGIN_URL, and remember the page asked for (?next=...) to come back to it after login
        return redirect_to_login(request.get_full_path())

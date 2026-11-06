from django.http import HttpResponse
# from django.http import HttpResponse
from django.shortcuts import render

# def my_fun_middleware(get_response):
#     print("One Time Initialization")
    
#     def my_func(request):
#         print("This is before view")
#         response = get_response(request)
#         print("this is after view")
#         return response
    
#     return my_func


# def my_fun_middleware(get_response):
#     print("One Time Initialization")
    
#     def my_func(request):
#         print("This is before view")
#         # response = HttpResponse("Response from my fun middleware")
#         response = render(request, 'blog/uc.html')
#         print("this is after view")
#         return response
    
#     return my_func


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):

        print("Before View")

        response = self.get_response(request)

        print("After View")

        return response


#three middlewares to see the order they run in
class MyMiddleware1:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Middleware 1 Initialization")

    def __call__(self, request):

        print("This is Middleware 1 before view")

        response = self.get_response(request)

        print("This is Middleware 1 after view")

        return response


class MyMiddleware2:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Middleware 2 Initialization")

    def __call__(self, request):

        print("This is Middleware 2 before view")

        response = self.get_response(request)

        print("This is Middleware 2 after view")

        return response


class MyMiddleware3:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Middleware 3 Initialization")

    def __call__(self, request):

        print("This is Middleware 3 before view")

        response = self.get_response(request)

        print("This is Middleware 3 after view")

        return response


#process_view runs after the url is matched, just before the view is called
class MyProcessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        print("This is Process View - Before View")
        #return HttpResponse("This is before view")  #a response here skips the view
        return None  #None = carry on to the view


#process_exception runs only when a view raises an error
class MyExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)  #shown instead of Django's error page


#process_template_response runs only when the view returns a TemplateResponse (like the user view),
#before the template is rendered, so the context can still be changed here
class MyTemplateResponseMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process Template Response from Middleware")
        response.context_data['name'] = 'Zarish Nasir'
        return response

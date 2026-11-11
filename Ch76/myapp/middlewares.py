import time

from asgiref.sync import iscoroutinefunction, markcoroutinefunction


# 1. Async-only FUNCTION middleware
#    Django checks these two flags to know what the middleware can handle.
#    Default is sync_capable=True, async_capable=False, so we change both.
def my_async_middleware(get_response):
    print("One Time Initialization - async function middleware")

    async def middleware(request):
        print("Async function middleware - before view")
        response = await get_response(request)   #await: the next step is async too
        print("Async function middleware - after view")
        return response

    return middleware

my_async_middleware.sync_capable = False
my_async_middleware.async_capable = True


# 2. Async-only CLASS middleware
class MyAsyncMiddleware:
    sync_capable = False
    async_capable = True

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization - async class middleware")
        #tell Django this object's __call__ is a coroutine (async)
        markcoroutinefunction(self)

    async def __call__(self, request):
        start = time.time()
        print("Async class middleware - before view")
        response = await self.get_response(request)
        print(f"Async class middleware - after view ({time.time() - start:.3f} seconds)")
        return response


# 3. Hybrid middleware: works under BOTH runserver (WSGI, sync) and Uvicorn (ASGI, async)
#    Django gives it a sync or async get_response, and it picks the matching __call__
class HybridMiddleware:
    sync_capable = True
    async_capable = True

    def __init__(self, get_response):
        self.get_response = get_response
        self.is_async = iscoroutinefunction(get_response)
        if self.is_async:
            markcoroutinefunction(self)
        print("One Time Initialization - hybrid middleware, async =", self.is_async)

    def __call__(self, request):
        if self.is_async:
            return self.__acall__(request)   #returns a coroutine; Django awaits it
        print("Hybrid middleware (sync) - before view")
        response = self.get_response(request)
        print("Hybrid middleware (sync) - after view")
        return response

    async def __acall__(self, request):
        print("Hybrid middleware (async) - before view")
        response = await self.get_response(request)
        print("Hybrid middleware (async) - after view")
        return response

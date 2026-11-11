import asyncio

from django.http import HttpResponse

# Create your views here.
#an async view, so the whole chain from server to view stays async under Uvicorn
async def home(request):
    print("i am the async home view")
    await asyncio.sleep(1)   #pretend to wait for something (an API, a file...)
    return HttpResponse("Hello from the async home view - check the terminal")

import asyncio
import time

import httpx
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello home page")

# async def home(request):
#     return HttpResponse("Hello home page")


# synchronous view: the 5 requests run one after another
def sync_view(request):
    start_time = time.time()
    responses = []
    for _ in range(5):
        response = httpx.get("https://jsonplaceholder.typicode.com/posts")
        responses.append(response.json())
    end_time = time.time()
    time_taken = end_time - start_time
    return JsonResponse({
        'status': 'success',
        'total_request': 5,
        'time_taken': f"{time_taken:.2f} seconds"
    })


# asynchronous view: the 5 requests run at the same time
async def async_view(request):
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        tasks = [client.get("https://jsonplaceholder.typicode.com/posts")
                 for _ in range(5)]
        responses = await asyncio.gather(*tasks)

    end_time = time.time()
    time_taken = end_time - start_time
    return JsonResponse({
        'status': 'success',
        'total_request': 5,
        'time_taken': f"{time_taken:.2f} seconds"
    })

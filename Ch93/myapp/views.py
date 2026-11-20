import asyncio
import time
import httpx
import requests
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View

# Create your views here.
# A free public API for practice, post 1 to post 5 are fetched by the two views.
API_URL = 'https://jsonplaceholder.typicode.com/posts/{}'
POST_IDS = [1, 2, 3, 4, 5]


# the same page for both views, so only the time is different
def result_page(heading, titles, seconds):
    items = ''.join(f'<li>{escape(title)}</li>' for title in titles)
    return HttpResponse(f'<h1>{heading}</h1><p>5 API calls took {seconds:.2f} seconds</p><ul>{items}</ul>')


class HomeView(View):
    def get(self, request):
        return HttpResponse('<h1>Sync and async class based views</h1>')


# A normal (sync) class based view: get() is a normal function and requests is a normal library.
# Each requests.get() waits for the answer and only then the loop goes to the next call,
# so the time is the 5 calls added together (about 5 x the time of one call).
class SyncView(View):
    def get(self, request):
        start = time.time()
        titles = []
        for post_id in POST_IDS:
            response = requests.get(API_URL.format(post_id), timeout=10)
            titles.append(response.json()['title'])
        return result_page('Sync view', titles, time.time() - start)


# An async class based view: async def get(), and httpx (requests can not be awaited).
# await gives the thread back while the answer is coming, and asyncio.gather starts all 5 calls together,
# so the time is only about the time of the slowest one call.
# All the methods of one view class must be the same kind: all def or all async def.
class AsyncView(View):
    async def get(self, request):
        start = time.time()
        async with httpx.AsyncClient() as client:
            responses = await asyncio.gather(
                *[client.get(API_URL.format(post_id), timeout=10) for post_id in POST_IDS]
            )
        titles = [response.json()['title'] for response in responses]
        return result_page('Async view', titles, time.time() - start)

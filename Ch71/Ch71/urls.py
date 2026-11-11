
from django.contrib import admin
from django.urls import path
from myapp.views import home, sync_view, async_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sync/', sync_view, name='sync_view'),
    path('async/', async_view, name='async_view'),
]

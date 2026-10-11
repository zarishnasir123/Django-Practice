from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('course/', include('course.urls')),
]
# include() is used to include the urls from the other apps
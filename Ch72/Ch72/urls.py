from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp.views import get_student_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', get_student_data)
]

#only while developing: Django itself serves the files collected in STATIC_ROOT
#(Uvicorn does not serve static files on its own)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #CKEditor 5 uploads images through this url
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', include('blog.urls')),
]

# serve uploaded files (media folder) while developing; only works when DEBUG = True
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

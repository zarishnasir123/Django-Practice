"""
URL configuration for Ch7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views as app1_views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # App1
    path('home/', app1_views.home, name='home'),
    path('about/', app1_views.about, name='about'),

    # App2
    path('app2/', app2_views.app2, name='app2'),
    path('app2home/', app2_views.app2home, name='app2home'),
]


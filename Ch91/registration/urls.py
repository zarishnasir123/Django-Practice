from django.urls import path
from registration import views

urlpatterns = [
    # the paths are added here when the views are written
    path('profile/', views.ProfileTemplateView.as_view(), name='profile')
]

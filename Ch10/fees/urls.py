from django.urls import path
from fees.views import fee_courses

urlpatterns = [
    path('', fee_courses, name='fee_courses')
]

from django.urls import path
from . import views

urlpatterns = [
    # the names are used by the views (success_url = reverse_lazy('studentlist')) and by the templates ({% url '...' %})
    path('', views.StudentListView.as_view(), name='studentlist'),
    # the three pages that work on one student need its pk, and it must be named pk
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='studentdetail'),
    path('create/', views.StudentCreateView.as_view(), name='studentcreate'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='studentupdate'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='studentdelete'),
]

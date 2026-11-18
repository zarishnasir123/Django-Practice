from django.urls import path
from . import views

urlpatterns = [
    # <int:pk> must be named pk: DetailView looks for the row with this pk
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    # the name here is id, not pk, so the view must say pk_url_kwarg = 'id'
    path('student1/<int:id>/', views.StudentDetailView1.as_view(), name='student_detail1'),
    path('student2/<int:pk>/', views.StudentDetailView2.as_view(), name='student_detail2'),
]

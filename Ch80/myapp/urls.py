from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListView.as_view(), name='students'),
    path('all/', views.AllStudentListView.as_view(), name='all_students'),
    path('student1/', views.StudentListView1.as_view(), name='students1'),
    path('student2/', views.StudentListView2.as_view(), name='students2'),
    path('student3/', views.StudentListView3.as_view(), name='students3'),
    
    
]

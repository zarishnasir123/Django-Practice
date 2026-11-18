from django.views.generic import DetailView
from .models import Student

# Create your views here.
# DetailView shows ONE row. It gets the row by itself: with model = Student it runs
# Student.objects.get(pk=...), where pk comes from the url: path('student/<int:pk>/')
# It sends the row to the template as "object" (and also as "student").
# It finds the template by name: <app>/<model>_detail.html = myapp/student_detail.html,
# so template_name is not needed.
# If no student has that pk, it shows a 404 page by itself.
class StudentDetailView(DetailView):
    model = Student


# pk_url_kwarg = the NAME the url uses for the pk. The default is 'pk' (that is why the
# first view needs <int:pk>). Here the url says <int:id>, so we tell the view to look for 'id'.
class StudentDetailView1(DetailView):
    model = Student
    pk_url_kwarg = 'id'


# template_name_suffix changes the end of the default template name.
# The default suffix is '_detail' (myapp/student_detail.html).
# With '_info' the view looks for myapp/student_info.html instead.
class StudentDetailView2(DetailView):
    model = Student
    template_name_suffix = '_info'

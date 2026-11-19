from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Student

# Create your views here.
# DeleteView removes ONE row. Like DetailView and UpdateView it finds the row by itself:
# the pk comes from the url: path('delete/<int:pk>/')
#  - GET  shows the "are you sure?" page: <app>/<model>_confirm_delete.html
#         (myapp/student_confirm_delete.html), the row is sent as "object" (and "student")
#  - POST (the button on that page) deletes the row and goes to success_url
# success_url is required: the row is gone, so there is no get_absolute_url() to go to.
# reverse_lazy is used (not reverse) because the urls are not loaded yet when this class is read.
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('thanks')

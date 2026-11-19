from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student



# Read: all the students (sent to the template as student_list / object_list)
class StudentListView(ListView):
    model = Student
    ordering = ['roll']


# Read: one student, the pk comes from the url (sent to the template as student / object)
class StudentDetailView(DetailView):
    model = Student


# Create: shows an empty form, a valid POST saves a new row and goes to success_url
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'roll']
    success_url = reverse_lazy('studentlist')


# Update: the same form, filled with the row found by pk
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'roll']
    success_url = reverse_lazy('studentlist')


# Delete: GET asks "are you sure?", a POST deletes the row and goes to success_url
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('studentlist')

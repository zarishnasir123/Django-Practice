from django.views.generic.edit import UpdateView
from .forms import StudentForm
from .models import Student

# Create your views here.
# UpdateView edits ONE row that already exists. Like DetailView it finds the row by itself:
# the pk comes from the url: path('update/<int:pk>/'), and the form arrives filled with the
# current values. Like CreateView it uses the template <app>/<model>_form.html
# (myapp/student_form.html) and, after a valid save, goes to Student.get_absolute_url().
class StudentUpdateView(UpdateView):
    model = Student           # which table the row is taken from
    form_class = StudentForm  # the fields and the styling

from django.views.generic import ListView
from .models import Student

# Create your views here.
# ListView gets the rows by itself: with model = Student it runs Student.objects.all()
# and sends them to the template as "object_list" (and also as "student_list").
# It also finds the template by name: <app>/<model>_list.html = myapp/student_list.html,
# so template_name is not needed.
class StudentListView(ListView):
    model = Student


#same rows, but the template is chosen with template_name instead of the default name
class AllStudentListView(ListView):
    model = Student
    template_name = 'myapp/student.html'

class StudentListView1(ListView):
    model = Student
    template_name_suffix = '_all'
    ordering = ['roll']
    
class StudentListView2(ListView):
    model = Student
    template_name = 'myapp/students.html'
    
    
class StudentListView3(ListView):
    model = Student
    template_name = 'myapp/sabhistudents.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        return Student.objects.filter(course = "Python")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["java_students"] = Student.objects.filter(course = "Java")
        return context
    
    def get_template_names(self):
        if self.request.COOKIES.get('user') == 'Umar':
            template_name = 'myapp/umar.html'
            
        else:
            template_name = self.template_name
        return [template_name]
    
from django.shortcuts import render
from student.forms import DemoForm

# Create your views here.
def demo_form(req):
    form = DemoForm()
    return render(req, 'student/demoform.html', {'form' : form})


from django.shortcuts import render
from student.forms import Registration, Login

# Create your views here.
def registration(req):
    fm = Registration(field_order=['email','city'])
    return render(req, 'student/registration.html', {'form' : fm})


def login(req):
    # fm = Login(auto_id=True)
    # fm = Login(label_suffix='')
    fm = Login(initial={'email': 'zarish@example.com'})
    return render(req, 'student/login.html', {'form' : fm})
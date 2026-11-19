from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from .forms import StudentForm

from django import forms

# Create your views here.
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     # success_url = '/thanks/'
#     template_name = 'myapp/register.html'
    
#     def get_form(self):
#         form = super().get_form()
#         form.fields['password'].widget = forms.PasswordInput()
#         return form


# The form class (fields + styling) now lives in forms.py, so the view only names it.
# After a valid save, CreateView goes to Student.get_absolute_url() (the thanks page),
# so success_url is not needed.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'myapp/register.html'
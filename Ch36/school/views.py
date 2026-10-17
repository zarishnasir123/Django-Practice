from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration, TeacherRegistration


def student_form(request):

    if request.method == 'POST':
        form = StudentRegistration(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/school/success/')

    else:
        form = StudentRegistration()

    return render(request, 'school/registration.html', {
        'title': 'Student Registration',
        'form': form
    })


def teacher_form(request):

    if request.method == 'POST':
        form = TeacherRegistration(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/school/success/')

    else:
        form = TeacherRegistration()

    return render(request, 'school/registration.html', {
        'title': 'Teacher Registration',
        'form': form
    })


def success(request):
    return render(request, 'school/success.html')

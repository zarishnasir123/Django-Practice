from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student

# Create your views here.

#home page: register form + list of students
def home(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            #SUCCESS message, long form (the short form is: messages.success(request, '...'))
            messages.add_message(request, messages.SUCCESS, 'Your account has been created')
            #redirect: the message is kept and shown on the next page (Post/Redirect/Get)
            return HttpResponseRedirect('/')

        else:
            #ERROR message: no redirect here, so it shows on this same page next to the field errors
            messages.error(request, 'Please correct the errors below.')

    else:
        form = StudentForm()

    students = Student.objects.order_by('-id')

    return render(request, 'student/home.html', {
        'form': form,
        'students': students
    })


#delete a student, then show a WARNING message
def delete_student(request, id):
    #only delete when the Delete button (a POST form) was used, never from a plain link
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        student.delete()
        messages.warning(request, f'Student "{student.name}" has been deleted.')

    return HttpResponseRedirect('/')


#one message of every level, to see how each one looks
def all_levels(request):
    #DEBUG (level 10): hidden by default; shown here because MESSAGE_LEVEL = DEBUG in settings.py
    messages.debug(request, 'Debug: messages.debug() - level 10')

    #INFO (level 20) with extra_tags: 'fw-bold' is an extra class (Bootstrap bold text)
    messages.info(request, 'Info: messages.info() with extra_tags="fw-bold" - level 20', extra_tags='fw-bold')

    #SUCCESS (level 25)
    messages.success(request, 'Success: messages.success() - level 25')

    #WARNING (level 30)
    messages.warning(request, 'Warning: messages.warning() - level 30')

    #ERROR (level 40): MESSAGE_TAGS in settings.py turns its tag into "danger" for Bootstrap
    messages.error(request, 'Error: messages.error() - level 40')

    #the long form works for every level: add_message(request, LEVEL, text)
    messages.add_message(request, messages.INFO, 'Long form: messages.add_message(request, messages.INFO, ...)')

    return HttpResponseRedirect('/')

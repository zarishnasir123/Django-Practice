from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

def student_form(request):

    if request.method == 'POST':
        #save data: every submit adds a new row
        form = StudentForm(request.POST)

        #update data: the form changes the row with id=1 instead of adding a new one
        # student = Student.objects.get(id=1)
        # form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()

            #delete data: removes the row with id=1 (comment out form.save() above when using this)
            # student = Student.objects.get(id=1)
            # student.delete()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # keep the data for the next page, because a redirect starts a new request
            request.session['name'] = name
            request.session['email'] = email

            return HttpResponseRedirect('/student/success/')

    else:
        form = StudentForm()

    return render(request, 'student/registration.html', {
        'form': form
    })


def success(request):
    return render(request, 'student/success.html', {
        'name': request.session.get('name'),
        'email': request.session.get('email')
    })
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

def student_form(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # student = Student(name=name, email=email, password=password)
            # student.save()

            #update data: id=2 already exists, so save() changes that row instead of adding a new one
            # student = Student(id=2, name=name, email=email, password=password)
            # student.save()

            #delete data: removes the row with id=4
            student = Student(id=4)
            student.delete()

            # keep the data for the next page, because a redirect starts a new request
            request.session['name'] = name
            request.session['email'] = email
            
            #save data into database
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
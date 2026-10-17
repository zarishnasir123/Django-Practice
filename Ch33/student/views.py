from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm

def student_form(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
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
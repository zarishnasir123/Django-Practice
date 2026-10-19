from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def home(request):

    if request.method == 'POST':
        #request.FILES carries the uploaded image and document
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = ProfileForm()

    candidates = Profile.objects.all()

    return render(request, 'student/home.html', {
        'form': form,
        'candidates': candidates
    })

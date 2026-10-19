from django.shortcuts import render, get_object_or_404
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


#one candidate's details; pk comes from the url
def candidate(request, pk):
    #shows a "Page not found" (404) instead of crashing when the id doesn't exist
    candidate = get_object_or_404(Profile, pk=pk)

    return render(request, 'student/candidate.html', {
        'candidate': candidate
    })

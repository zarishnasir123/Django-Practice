from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'data' : 'Hello, I am Django Developer. I am also creating educational videos. I am not human'}
    return render(request, 'student/home.html', context)

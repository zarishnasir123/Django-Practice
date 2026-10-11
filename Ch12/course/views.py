from django.shortcuts import render

# Create your views here.
#Example 1.1 - Variable

# def learn_django(req):
#     return render(req, 'course/django.html', context={'name': 'Django'})

#Example 1.2 - Dictionary
def learn_django(req):
    name = 'Django'
    duration = '4 months'
    seats = 10
    course_details = {
        'name': name,
        'duration': duration,
        'seats': seats
    }
    return render(req, 'course/django.html', context=course_details)
from django.shortcuts import render
from datetime import datetime

#Example 1.3 - DateTime
def learn_django(req):
    name = 'Django'
    duration = '4 months'
    date = datetime.now()
    return render(req, 'course/django.html', context={'name': name, 'duration': duration, 'date': date})

# Create your views here.
#Example 1.1 - Variable

# def learn_django(req):
#     return render(req, 'course/django.html', context={'name': 'Django'})

#Example 1.2 - Dictionary
# def learn_django(req):
#     name = 'Django'
#     duration = '4 months'
#     seats = 10
#     course_details = {
#         'name': name,
#         'duration': duration,
#         'seats': seats
#     }
#     return render(req, 'course/django.html', context=course_details)

# #Example 2: Filter
# def learn_django(req):
#    return render(req, 'course/django.html', context={'name': 'Django', 'desc': 'Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.'})

# #Example 3: Date time
# def learn_django(req):
#     d = datetime.now()
#     return render(req, 'course/django.html', context={'name': 'Django', 'dt': d})

# #Example 4: Float format
# def learn_django(req):
#     return render(req, 'course/django.html', context={'p1': 56.24321, 'p2': 56.000, 'p3': 56.37000})

# #Example 4: If Tag
# def learn_django(req):
#     nm = True
#     return render(req, 'course/django.html', context={'nm' : True})

# #Example 5: For Tag
# def learn_django(req):
#     student = {'names': ['zarish', 'zohaib', 'ali', 'ahsan', 'umar']}
#     return render(req, 'course/django.html', context=student)

#Example 7

# def learn_django(request):
#     stu = {
#         'stu1': {'name': 'Ali', 'roll': 1},
#         'stu2': {'name': 'Ahmed', 'roll': 2},
#         'stu3': {'name': 'Sara', 'roll': 3},
#         'stu4': {'name': 'Zarish', 'roll': 4},
#     }

#     students = {'student': stu}

#     return render(request, 'course/django.html', context = students)

# #example 8
# def learn_django(request):
#     stu = {
#         'name': 'Ali',
#         'roll': 1,
#     }

#     student = {'students': [stu]}

#     return render(request, 'course/django.html', context=student)

#Example 9
from django.shortcuts import render

def learn_django(request):
    stu = [
        {
            'name': 'Ali',
            'roll': 1,
            'age': 21,
            'address': {
                'city': 'Lahore',
                'country': 'Pakistan',
            },
            'marks': 85,
            'subjects': ['Python', 'Django', 'Database'],
            'skills': ['HTML', 'CSS', 'JavaScript'],
        },
        {
            'name': 'Sara',
            'roll': 2,
            'age': 22,
            'address': {
                'city': 'Gujranwala',
                'country': 'Pakistan',
            },
            'marks': 92,
            'subjects': ['Python', 'AI', 'Database'],
            'skills': ['React', 'Python', 'MySQL'],
        },
    ]

    student = {'students': stu}

    return render(request, 'course/django.html', context=student)
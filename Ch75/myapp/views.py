from django.shortcuts import render
from .models import Student

# Create your views here.
# async ORM: the async versions of ORM methods start with "a" and are awaited
async def home(request):
    #async for: go through a QuerySet without blocking
    #(the rows are collected in a list, because the template loop itself is synchronous)
    students = []
    async for student in Student.objects.all():
        print(student.name, student.email, student.age)
        students.append(student)

    #acount(): how many rows
    total = await Student.objects.acount()
    print("Total students:", total)

    #afirst(): the first row (None if the table is empty)
    first = await Student.objects.afirst()
    print("First student:", first)

    return render(request, 'myapp/home.html', {'students': students, 'total': total, 'first': first})

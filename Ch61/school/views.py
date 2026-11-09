from django.shortcuts import render
from .models import Student

# Create your views here.
# Limiting a QuerySet uses Python slicing [start:stop]; Django turns it into SQL LIMIT / OFFSET.
# Uncomment ONE student_data line at a time; the terminal shows the result and the SQL.
def home(request):

    #first 5 rows -> LIMIT 5
    student_data = Student.objects.all()[:5]

    #rows 6 to 10 (start counts from 0) -> LIMIT 5 OFFSET 5
    # student_data = Student.objects.all()[5:10]

    #skip the first 3, take the rest -> OFFSET 3
    # student_data = Student.objects.all()[3:]

    #top 3 marks: order first, then slice
    # student_data = Student.objects.order_by('-marks')[:3]

    #last 3 students: negative slicing like [-3:] is NOT allowed, so reverse the order instead
    # student_data = Student.objects.order_by('-id')[:3]

    #slice after filter: first 2 students from Lahore
    # student_data = Student.objects.filter(city='Lahore')[:2]

    #one index gives ONE object, not a QuerySet -> send {'stu': ...}
    #(IndexError if that row does not exist)
    # student_data = Student.objects.all()[0]

    #a step like [::2] runs the query at once and gives a plain list, not a QuerySet
    # student_data = Student.objects.all()[:10:2]

    print("Return:", student_data)
    print()
    #only a QuerySet has .query (a single object or a list does not)
    if hasattr(student_data, 'query'):
        print("SQL Query:", student_data.query)

    return render(request, 'school/home.html', {'students': student_data})

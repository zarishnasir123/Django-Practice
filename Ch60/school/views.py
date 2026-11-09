from django.db.models import Q
from django.shortcuts import render
from .models import Student


def home(request):

    #&  AND: both conditions true (same as filter(city='Lahore', marks=80))
    student_data = Student.objects.filter(Q(city='Lahore') & Q(marks=80))

    #|  OR: either condition true
    # student_data = Student.objects.filter(Q(city='Lahore') | Q(city='Karachi'))

    #~  NOT: everyone except the match (like exclude)
    # student_data = Student.objects.filter(~Q(city='Lahore'))

    #Q works with field lookups too
    # student_data = Student.objects.filter(Q(marks__gte=90) | Q(name__startswith='A'))

    #brackets decide the order: (Lahore OR Karachi) AND marks >= 80
    # student_data = Student.objects.filter((Q(city='Lahore') | Q(city='Karachi')) & Q(marks__gte=80))

    #NOT with OR: neither Lahore nor Karachi
    # student_data = Student.objects.filter(~(Q(city='Lahore') | Q(city='Karachi')))

    #Q mixed with a normal keyword argument: the Q must come FIRST
    # student_data = Student.objects.filter(Q(city='Lahore') | Q(city='Islamabad'), marks=70)

    #Q in exclude(): remove everyone who is from Lahore OR has less than 70
    # student_data = Student.objects.exclude(Q(city='Lahore') | Q(marks__lt=70))

    #Q in get(): must still match exactly one row
    # student_data = Student.objects.get(Q(roll=101) & Q(city='Lahore'))

    #building a Q step by step, e.g. from a search box
    # search = Q()
    # for city in ['Lahore', 'Multan']:
    #     search |= Q(city=city)
    # student_data = Student.objects.filter(search)

    print("Return:", student_data)
    print()
    print("SQL Query:", student_data.query)

    return render(request, 'school/home.html', {'students': student_data})

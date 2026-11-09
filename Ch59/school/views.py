from django.db.models import Avg, Count, Max, Min, Sum
from django.shortcuts import render
from .models import Student

# Create your views here.
# aggregate() runs ONE calculation over many rows and returns a dictionary, not a QuerySet.
def home(request):
    student_data = Student.objects.all()

    #default key names are field__function, e.g. {'marks__avg': 77.0}
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    count = student_data.aggregate(Count('marks'))
    print(average, total, minimum, maximum, count)

    #all in one query, with my own key names
    result = student_data.aggregate(
        avg_marks=Avg('marks'),
        total_marks=Sum('marks'),
        min_marks=Min('marks'),
        max_marks=Max('marks'),
        total_students=Count('id'),
    )
    print(result)

    #filter first, then aggregate: only the Lahore students
    lahore = Student.objects.filter(city='Lahore').aggregate(avg_marks=Avg('marks'), total_students=Count('id'))
    print(lahore)

    #distinct=True counts each different value once: how many different cities
    cities = student_data.aggregate(total_cities=Count('city', distinct=True))
    print(cities)

    #annotate(): adds a calculated value to EVERY row and returns a QuerySet (aggregate gives one dictionary)
    #values('city') before annotate = GROUP BY city, so each city gets its own count and average
    city_report = Student.objects.values('city').annotate(
        total_students=Count('id'),
        avg_marks=Avg('marks'),
        max_marks=Max('marks'),
    ).order_by('city')
    print(city_report)

    context = {
        'students': student_data,
        'average': average,
        'total': total,
        'minimum': minimum,
        'maximum': maximum,
        'count': count,
        'result': result,
        'lahore': lahore,
        'cities': cities,
        'city_report': city_report,
    }
    return render(request, 'school/home.html', context)

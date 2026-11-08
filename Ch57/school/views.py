from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):

    #-------- return ONE object -> {'stu': ...} --------

    #get(): exactly one row; DoesNotExist if none, MultipleObjectsReturned if more than one
    # student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.get(roll=105)

    #first() / last(): first or last row (by id, or by order_by); None if the table is empty
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.last()

    #latest() / earliest(): newest or oldest by a date field
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')

    #-------- return a QuerySet -> {'students': ...} --------
    student_data = Student.objects.order_by('name')

    #-------- return True / False --------

    #exists(): is there at least one matching row? (faster than counting)
    # student_data = Student.objects.filter(city='Lahore').exists()

    #contains(): is this exact object in the queryset?
    # one = Student.objects.get(pk=1)
    # student_data = Student.objects.filter(city='Lahore').contains(one)

    #-------- return a number --------

    #count(): how many rows (SELECT COUNT(*))
    # student_data = Student.objects.count()
    # student_data = Student.objects.filter(marks=90).count()

    #update(): changes every matching row, returns how many rows changed
    #(it runs on every page refresh, so use it once and comment it again)
    # student_data = Student.objects.filter(city='Multan').update(marks=85)

    #-------- return a dictionary --------

    #in_bulk(): {id: object} for the given ids
    # student_data = Student.objects.in_bulk([1, 2, 3])

    #aggregate(): one calculation over all rows, e.g. {'marks__avg': 77.0}
    # from django.db.models import Avg, Max, Min, Sum
    # student_data = Student.objects.aggregate(Avg('marks'), Max('marks'), Min('marks'), Sum('marks'))

    #-------- create / save --------
    #(these add rows on every refresh; roll is unique, so a second refresh gives IntegrityError)

    #create(): makes and saves a row in one step, returns the object -> {'stu': ...}
    # student_data = Student.objects.create(name='Noor Fatima', roll=111, city='Lahore', marks=75, pass_date='2024-08-01')

    #get_or_create(): returns (object, created); created=False if it was already there
    # student_data, created = Student.objects.get_or_create(name='Noor Fatima', roll=111, city='Lahore', marks=75, pass_date='2024-08-01')
    # print("created:", created)

    #update_or_create(): finds by roll, updates the defaults, creates if not found -> (object, created)
    # student_data, created = Student.objects.update_or_create(roll=111, defaults={'marks': 95})
    # print("created:", created)

    #bulk_create(): saves many objects in one query, returns the list
    # student_data = Student.objects.bulk_create([
    #     Student(name='Ahmed Ali', roll=112, city='Karachi', marks=65, pass_date='2024-08-02'),
    #     Student(name='Sara Imran', roll=113, city='Multan', marks=88, pass_date='2024-08-02'),
    # ])

    #-------- delete --------

    #delete(): removes matching rows, returns (total deleted, {model: count})
    # student_data = Student.objects.filter(roll__gte=111).delete()

    print("student data", student_data)

    return render(request, 'school/home.html', {'students': student_data})

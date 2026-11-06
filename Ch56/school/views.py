from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.
# QuerySet methods: each one returns a new QuerySet, so they can be chained.
# Uncomment ONE student_data line at a time and watch the terminal (result + SQL).
def home(request):

    #all(): every row of the table
    student_data = Student.objects.all()

    #filter(): only rows that match
    # student_data = Student.objects.filter(marks=80)

    #exclude(): every row EXCEPT the ones that match
    # student_data = Student.objects.exclude(marks=80)

    #order_by(): sort ascending, '-' for descending, '?' for random
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')

    #order_by() with two fields: same marks are then sorted by name
    # student_data = Student.objects.order_by('marks', 'name')

    #reverse(): flips an ordered queryset (needs order_by first)
    # student_data = Student.objects.order_by('id').reverse()

    #slicing: like LIMIT/OFFSET in SQL (first 5 rows); negative index is not allowed
    # student_data = Student.objects.order_by('id')[:5]

    #values(): dictionaries instead of objects, {'name': ..., 'city': ...}
    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city')

    #values_list(): tuples instead of dictionaries, ('Ali Raza', 'Lahore')
    # student_data = Student.objects.values_list('id', 'name')
    #named=True gives tuples that can be read like stu.name
    # student_data = Student.objects.values_list('id', 'name', named=True)
    #flat=True with one field gives a plain list ['Ali Raza', ...]
    # student_data = Student.objects.values_list('name', flat=True)

    #distinct(): removes duplicate rows (use with values so only those fields are compared)
    # student_data = Student.objects.values('city').distinct()

    #dates(): the different dates of a DateField, rounded to 'year', 'month' or 'day'
    # student_data = Student.objects.dates('pass_date', 'month')

    #none(): an empty queryset; no SQL is made, so "print(student_data.query)" below raises EmptyResultSet
    # student_data = Student.objects.none()

    #only(): load just these fields now (others load later if used)
    # student_data = Student.objects.only('name', 'roll')

    #defer(): load every field except these
    # student_data = Student.objects.defer('pass_date')

    #using(): pick which database to run on (name from DATABASES in settings)
    # student_data = Student.objects.using('default')

    #-------- set operations: both querysets must have the same fields --------
    #union(): rows from both tables, duplicates removed (all=True keeps them)
    # qs1 = Student.objects.values_list('name', 'city')
    # qs2 = Teacher.objects.values_list('name', 'city')
    # student_data = qs1.union(qs2)
    # student_data = qs1.union(qs2, all=True)

    #intersection(): only rows that are in BOTH (Ali Raza, Ayesha Khan, Hamza Sheikh)
    # student_data = qs1.intersection(qs2)

    #difference(): rows in the first that are NOT in the second (students who aren't teachers)
    # student_data = qs1.difference(qs2)

    #-------- AND / OR --------
    #& means both conditions (AND), | means either one (OR)
    # student_data = Student.objects.filter(city='Lahore') & Student.objects.filter(marks=80)
    # student_data = Student.objects.filter(city='Lahore') | Student.objects.filter(city='Karachi')

    #chaining: filter + exclude + order_by together
    # student_data = Student.objects.filter(city='Lahore').exclude(marks=60).order_by('-marks')

    print("Return:", student_data)
    print()
    #.query shows the SQL Django builds
    print("SQL Query:", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

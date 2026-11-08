from django.shortcuts import render
from .models import Student

# Create your views here.
# Field lookups go inside filter() / exclude() / get() as  field__lookup=value  (two underscores).
# Every one returns a QuerySet, so the template gets {'students': ...}.
# Uncomment ONE student_data line at a time; the terminal shows the result and the SQL.
def home(request):

    #-------- text --------

    #exact: equal, case-sensitive (same as filter(name='Ali Raza'))
    student_data = Student.objects.filter(name__exact='Ali Raza')

    #iexact: equal, ignoring capital/small letters
    # student_data = Student.objects.filter(name__iexact='ali raza')

    #contains / icontains: text appears anywhere (i = ignore case)
    # student_data = Student.objects.filter(name__contains='Khan')
    # student_data = Student.objects.filter(name__icontains='khan')

    #startswith / istartswith: text at the beginning
    # student_data = Student.objects.filter(name__startswith='H')
    # student_data = Student.objects.filter(city__istartswith='la')

    #endswith / iendswith: text at the end
    # student_data = Student.objects.filter(name__endswith='Malik')
    # student_data = Student.objects.filter(city__iendswith='BAD')

    #-------- lists and ranges --------

    #in: value is one of the list
    # student_data = Student.objects.filter(id__in=[1, 3, 5])
    # student_data = Student.objects.filter(city__in=['Lahore', 'Multan'])

    #range: between two values, both included (SQL BETWEEN)
    # student_data = Student.objects.filter(marks__range=(70, 85))

    #-------- numbers --------

    #gt / gte / lt / lte: greater than, greater or equal, less than, less or equal
    # student_data = Student.objects.filter(marks__gt=80)
    # student_data = Student.objects.filter(marks__gte=80)
    # student_data = Student.objects.filter(marks__lt=70)
    # student_data = Student.objects.filter(marks__lte=70)

    #-------- dates --------

    #date fields can be compared like numbers
    # student_data = Student.objects.filter(pass_date__gt='2024-06-01')
    # student_data = Student.objects.filter(pass_date__range=('2024-05-01', '2024-06-30'))

    #year / month / day: one part of the date
    # student_data = Student.objects.filter(pass_date__year=2024)
    # student_data = Student.objects.filter(pass_date__month=6)
    # student_data = Student.objects.filter(pass_date__day=10)

    #parts can be combined with gt/gte/lt/lte too
    # student_data = Student.objects.filter(pass_date__month__gte=6)

    #week / week_day / quarter: week of the year, day of the week (1 = Sunday ... 7 = Saturday), quarter 1-4
    # student_data = Student.objects.filter(pass_date__week=22)
    # student_data = Student.objects.filter(pass_date__week_day=6)
    # student_data = Student.objects.filter(pass_date__quarter=3)

    #-------- empty values and patterns --------

    #isnull: True = field is empty (NULL), False = has a value
    # student_data = Student.objects.filter(city__isnull=False)

    #regex / iregex: matches a regular expression
    # student_data = Student.objects.filter(name__regex=r'^(A|H)')
    # student_data = Student.objects.filter(city__iregex=r'(lahore|karachi)$')

    #-------- combined --------

    #several lookups in one filter = AND
    # student_data = Student.objects.filter(city='Lahore', marks__gte=80)

    #exclude() with a lookup: everyone except these
    # student_data = Student.objects.exclude(marks__lt=70)

    print("Return:", student_data)
    print()
    print("SQL Query:", student_data.query)

    return render(request, 'school/home.html', {'students': student_data})

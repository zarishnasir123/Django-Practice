from django.urls import path, register_converter
from student.views import home, profile, student_subject, subject_detail, student_by_name, result
from .converters import RollNumberConverter

#custom converter: use it in a url as <roll:...>
register_converter(RollNumberConverter, 'roll')


urlpatterns = [
    path('', home, name='home'),
    #int: numbers only, and the view gets a real number
    path('profile/<int:my_id>/', profile, name='profile'),
    #two values in one url
    path('profile/<int:my_id>/subject/<int:sub_id>/', student_subject, name='student_subject'),
    #slug: letters, numbers, - and _ (no spaces)
    path('subject/<slug:subject>/', subject_detail, name='subject'),
    #str: any text without /
    path('student/<str:name>/', student_by_name, name='student_name'),
    #roll: custom converter from converters.py, e.g. /result/2026-CS-014/
    path('result/<roll:roll_no>/', result, name='result'),
]

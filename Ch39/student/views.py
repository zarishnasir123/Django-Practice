from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'student/home.html')


def profile(request, my_id):
    student = {'id' : my_id}
    return render(request, 'student/profile.html', student)


def student_subject(request, my_id, sub_id):
    return render(request, 'student/subject.html', {'id': my_id, 'sub_id': sub_id})


def subject_detail(request, subject):
    return render(request, 'student/subject_detail.html', {'subject': subject})


def student_by_name(request, name):
    return render(request, 'student/student_name.html', {'name': name})


#roll_no arrives already checked and in capitals by RollNumberConverter.to_python()
def result(request, roll_no):
    return render(request, 'student/result.html', {'roll_no': roll_no})


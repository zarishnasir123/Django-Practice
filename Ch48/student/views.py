from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['fname'] = 'zarish'
    request.session['lname'] = 'nasir'
    return render(request, 'student/setsession.html')

def getsession(request):
    fname = request.session.get('fname', 'Guest')
    lname = request.session.get('lname', '')
    return render(request, 'student/getsession.html', {'fname': fname, 'lname': lname})

def clearsession(request):
    request.session.flush()
    return render(request, 'student/clearsession.html')

from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['fname'] = 'zarish'
    request.session['lname'] = 'nasir'
    # request.session.set_expiry(0)
    return render(request, 'student/setsession.html')

def getsession(request):
    #.get() gives the default instead of a KeyError when the key is missing
    firstname = request.session.get('fname', 'Guest')
    lastname = request.session.get('lname', '')
    return render(request, 'student/getsession.html', {'firstname': firstname, 'lastname': lastname})


def delsession(request):
    if 'lname' in request.session:
        del request.session['lname']
    return render(request, 'student/delsession.html')

def flushsession(request):
    request.session.flush()
    return render(request, 'student/flushsession.html')

def sessionclear(request):
    request.session.clear_expired()
    return render(request, 'student/sessionclear.html')

def sessionmethodsinview(request):
    keys = request.session.keys()
    print(keys)
    items = request.session.items()
    print(items)
    age = request.session.setdefault('age', 31)
    print(age)
    
    session_cookie_age = request.session.get_session_cookie_age()
    print("session cookie age", session_cookie_age)
    
    expire_age = request.session.get_expiry_age()
    print("Expiry age", expire_age)
    
    expire_date = request.session.get_expiry_date()
    print("Expiry date", expire_date)
    
    expire_at_browser_close = request.session.get_expire_at_browser_close()
    print(expire_at_browser_close)
    
    
    return render(request, 'student/sessionmethodsinview.html')

def sessionmethodsintemplate(request):
     keys = request.session.keys()
     print(keys)
     items = request.session.items()
     print(items)
     return render(request, 'student/sessionmethodsintemplate.html', {'keys' : keys, 'items': items})

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')

def deletetestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deletetestcookie.html')

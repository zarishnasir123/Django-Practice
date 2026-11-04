from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def course(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'The One', 60)
#         mv = cache.get('movie')
        
#     return render(request, 'student/course.html', {'mv':mv})


#simple way to get n set at same time
# def course(request):
#     mv = cache.get_or_set('movie', 'The One', 60)
#     mv1 = cache.get_or_set('movie', 'The Harry', 60, version=2)
#     return render(request, 'student/course.html', {'mv':mv, 'mv1':mv1})

# def course(request):
#     data = {'name':'zarish', 'roll':101}
#     cache.set_many(data, 30)
#     stu = cache.get_many(data)
#     return render(request, 'student/course.html', {'stu':stu})


# def course(request):
#     cache.delete('movie', version=2)
#     return render(request, 'student/course.html')

# def course(request):
#     i = cache.incr('roll', delta=2)
#     return render(request, 'student/course.html')

def course(request):
    cache.clear()
    return render(request, 'student/course.html')

from django.shortcuts import render
from django.http import JsonResponse
from asgiref.sync import sync_to_async, async_to_sync
from myapp.models import Student

# Create your views here.
def my_sync_function1(x):
    return x*2

async def my_async_function1():
    result = await sync_to_async(my_sync_function1)(5)
    print(result)
    
#asynch to sync
async def my_async_function2(x):
    return x*2

def my_sync_function():
    result = async_to_sync(my_async_function2)(5)
    print(result)
    
# def get_student_data():
#     return list(Student.objects.filter(age=77).values())


# async def student_data(request):
#     student_data = await sync_to_async(get_student_data)()
#     return JsonResponse({
#         'data' : student_data
#     })

async def get_student_data(request):
    student_data = await sync_to_async(lambda: list(Student.objects.filter(age=77).values()))()
    return JsonResponse({
       'data' : student_data
    })
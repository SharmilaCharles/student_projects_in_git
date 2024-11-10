from django.http import HttpResponse
from django.shortcuts import render
from students.models import Students


def home(request):
    students = Students.objects.all()
    # print(students)
    context = {
        'students' : students
    }
    return render(request,'index.html', context)

    ''' 
    The purpose of context is to bridge data from your views 
    to your templates. Any data added to context can be accessed 
    in the template, enabling you to create dynamic web pages. 
    '''
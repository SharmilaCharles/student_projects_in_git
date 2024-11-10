from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

from students.models import Students

# Create your views here.
def StuApp_detail(request, pk):
    studentObj = get_object_or_404(Students,pk=pk)
    # print(studentObj)
    context = {
        'studentObj' : studentObj,
    }
    return render(request,'detailed_view.html',context)

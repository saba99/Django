
from django.Http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Course, Student, Teacher


def index(request):

    all_stusent=Student.objects.all().count() 

    all_teacher=Teacher.objects.all().count()

    all_course=Course.objects.all().count() 

    context={
        'all_student':all_student,
        'all_teacher':all_teacher,
        'all_course':all_course
    } 
    return render(request,'index.html',context) 

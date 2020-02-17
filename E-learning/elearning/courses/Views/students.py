from django.Http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Course, Student, Teacher



class StudentListView(generic.ListView):
    
    model=Student
    context_object_name='student'
    context={
        'name':'my name',
        'family':'my family'
    } 
    template_name='templates/student.html'

    def get_queryset(self,**kwargs):
    
        queryset=Student.objects.all()\
            .select_related('Course','Cname')\
            .order_by('family') 

        return queryset

class MyCourseListView(generic.ListView):

    model=Course 
    context_object_name='courses'
    context={

        'Cname':'My Courses'
    } 
    template_name='templates/course.html'

    def get_queryset(self):

        queryset=self.request.user.student.Courses\
            .select_related('Course','Cname')\
            .order_by('created') 

        return queryset

class MyLessonListView(generic.ListView):

    model=Lesson 
    context_object_name='lesson'
    context={
        'title':'My lessons'
    } 
    template_name='templates/lesson.html'  

    def get_queryset(self,**kwargs):

        
        return Course.objects.select_related('grouping')\
                        .order_by('created') 

class QuizeListView(generic.ListView): 

    model=Quize 
    context_object_name='quize'
    template_name='templates/quize.html'  

    def get_queryset(self):
        student=self.request.user.student
        queryset=Quize.objects.all()
        return queryset 
class TakenQuizeListView(generic.ListView):
    model = TakenQuize
    context_object_name = 'taken_quize'
    template_name = 'templates/takenquize.html'

    def get_queryset(self):
        student = self.request.user.student.taken_quize
        queryset = Quize.objects.all()
        return queryset 

def register(request):          
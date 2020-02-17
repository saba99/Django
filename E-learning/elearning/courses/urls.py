from django.urls import path,re_path ,include

from . import views 
from .Views import  students,teachers,staff

app_name='courses' 

urlpatterns=[

path('student/',include(([
    path('', students.MyCourseListView.as_view()),
    path('taken/', students.TakenQuizeListView.as_view()),
    path('lesson/', students.MyLessonListView.as_view()),
   
],

),namespace='students')),
path('teacher',include(([
    path('', teachers.CourseCreatedView.as_view()),
    path('courseupdate/', teachers.CouresUpdateView.as_view()),
    path('enrollview/', teachers.EnrollmentRequestsListView.as_view()),
    path('lessonview/', teachers. LessonListView.as_view()),
    path('quizeview/', teachers.QuizeListView.as_view()),
    path('quizeresult/', teachers.QuizeResultView.as_view())
    
],

), namespace='teachers')),
    path('staff', include(([
        path('', staff.AdminCreateView.as_view()),
        path('courseupdate/', staff.AdminListView.as_view()),
        path('enrollview/', staff.CouresListView.as_view()),
        path('lessonview/', staff.StudentListView.as_view()),
        path('quizeview/', staff.TeacherListView.as_view())
       

    ],

    ), namespace='teachers')),
    
    
    

]


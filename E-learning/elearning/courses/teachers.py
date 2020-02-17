from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.geneic import CreateView, ListView, UpdateView
from django.utils.decorators import method_decorator
from .forms import AdminAddForm, UserUpdateForm


class CourseCreatedView(CreateView):

    model=Course
    form_class=CourseAddForm
    template_name='templates/course_add_form.html'
    context={
        'title':'New Course'
    }
    def form_valid(self,form):
        course=form.save(commit=False)
        course.owner=self.request.user
        course.save()
class CouresListView(ListView):
    
    model=Course 
    context_object_name='course' 
    context={
        'title':'course',
    } 
    template='templates/course_list.html'
    def get_context_data(self, **kwargs):

        kwargs['courses']=self.request.user.courses\
        
        return super().def get_context_data(**kwargs)


class CouresUpdateView(ListView):

    model = Course
    fields=('title','code','subject','')
    context_object_name = 'course'
    context = {
        'title': ' Edit course',
    }
    template = 'templates/course_list.html'
    def get_queryset(self):

        return self.request.user.courses.all()
    def get_success_url(self):

        title=self.get_object() 
        message.success(self.request)
        return reverse('teachers:course_change_list')
class EnrollmentRequestsListView(ListView) :

    model=Course
    context_object_name='taken_courses'  
    context={
        'title':'Enrollment Requests'
    }
    template_name='templates/enrollment_list.html' 

    def get_queryset(self):

        return TakenCourse.objects.filter()  
class LessonListView(ListView):
    model=Lesson 
    context_object_name='lessons' 
    context={
        'title':'my lessons'
    } 
    def get_queryset(self):
        return lesson.objects.filter(course__in=self.request.user.courses.all()).order_by('title')
class QuizeListView(ListView):
    model=Quize
    context_object_name='quize' 
    template_name='templates/quize_results.html' 
    def  get_queryset(self):
        queryset=Quize.objects.filter(course__owner=self.request.user)\
            .order_by('title')
        return queryset 
class QuizeResultView(ListView):

    model = Quize
    context_object_name = 'quize'
    template_name='templates/quize_result.html' 
    def  get_context_data(self, **kwargs):
        
        return super(). get_context_data(**kwargs)
    def form_valid(self,form):
        user=form.save()       









@login_required
@teacher_required
def add_lesson(request):
    if request.method=='POST':
        form=LessonAddForm(request.user,data=request.POST)
        if form.is_valid():
            lesson=form.save(commit=False)
            lesson.save()
            message.success(request,'The lesson was successfuly created')
    else:
        form=LessonAddForm(current_user=request.user) 
    context={
        'form':form,
        'title':'Add a lesson'
    }   
    return render(request,'templates/lesson_add_form.html',context) 

def add_quize(request):
    if request.methode=='POST':
        form=Quize.AddForm(request.user,data=request.POST) 
        if form.is_valid():
            question=form.save(commit=False)
            question.save()
            message.success(
                request, 'The quiz was successfully created. You may now add some questions.')
    else:
        form=QuestionAddForm(current_user=request.user)
    context={
        'form':form,
        'title':'add a quize'
    }    


def register(request) :
    if request.user.is_authenticated:
        return redirect('index')  
    else:
        request.method=='POST' 
        form=TeacherSignUpForm(request.Post) 
        if form.is_valid():
            user=form.save()
            user.is_active=False 
            user.save() 







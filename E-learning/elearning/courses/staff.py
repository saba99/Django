from django.contrib import messages
from  django.contrib.auth.decorators import login_required
from django.views.geneic import  CreateView,ListView,UpdateView 
from django.utils.decorators import method_decorator
from .forms import AdminAddForm,UserUpdateForm   

@method_decorator([login_required,superuser_required])
class AdminCreateView(CreateView):
    model=User 
    form_class=AdminAddForm 
    template_name='templates/admin_add_form.html' 
    context={

    }
    def form_valid(self,form):
        user=form.save(commit=False)
        user.save() 
        message.success(self.request,'the admin account has been successfuly')

class AdminListView(ListView):
    model=User
    context_object_name='admin' 
    context={
        ''
    } 
    template='templates/admin_list.html'
    def get_queryset(self):

        return user.objects.filter(is_staff=True,is_active=True) \
            .order_by('username') 
class CouresListView(ListView):

    model=Course 
    context_object_name='course' 
    context={
        'title':'course',
    } 
    template='templates/course_request.html'
    def get_queryset(self):

        return course.objects.filter()
class StudentListView(ListView):
    
    model=Course 
    context_object_name='course' 
    context={
        'title':'students',
        'sidebar':'student_list'
    } 
    template='templates/Student_list.html'
    def get_queryset(self):

        return course.objects.filter()
class TeacherListView(ListView):
    
    model=User
    context_object_name='teacher' 
    context={
        'title':'Teachers',
        'sidebar':'teacher_list'
    } 
    template='templates/teacher_list.html'
    def get_queryset(self):

        return course.objects.filter(is_teacher=True,is_active=True)/
        .order_by('username')
def accept_course(request,course_pk):

    Course.objects.filter(id=course_pk).update(status='approved')  
def dashboard(request):
    context={
        'title':'Admin',
        'sidebar':'dashboard'
    }            



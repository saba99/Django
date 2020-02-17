from django.shortcuts import render,redirect
from django.views. generic import DeleteView,ListView
from django.contrib.auth import authenticate,login,logout
from .forms import SearchCourses,UserLoginForm 
from .models import Quize,Lesson,Course,TakenQuize 

class CourseDetailView(DeleteView):

    model=Course 
    context_object_name='course'
    template_name='templates/course_details.html'
    def get_context_data(self, **kwargs):
        student=None
        teacher=None 
        if self.user.authenticated:
            if self.request.user.is_student:
                student=self.request.user.student.taken_courses.filter(Course__id=self.kwargs['pk']).first()
                teacher=None 
            elif self.request.user.is_teacher:

                teacher=self.request.user.courses.filter(id=self.kwargs['pk']).first()
                student=None 
        return super().get_context_data(**kwargs) 

def about(request): 
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return  redirect('teachers:course_change_list')
        elif request.user.is_student:
            return redirect('students:mycourses_list') 
    return render(request,'classroom/about.html',{'title':'about us'}) 

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:course_change_list') 
        elif request.user.is_student:
            return redirect('students:mycourses_list') 
        elif request.user.is_staff:
            return redirect('staff:dashboard') 
    return render(request,'templates/home.html')

def login_view(request):
    next=request.GET.get('next')
    form=UserLoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('home') 
    else:
      if  form.is_valid():
            username=form.cleaned_data('username')
            password=form.cleaned_data('password')
            user=authenticate(username=username ,password=password)
            login(request,user)
            if next:
                return redirect(next)
            else:
                return redirect('/')
    return render(request,'authentication/login.html',{'form':form,'title':'login'})

def logout_view(request):  
    logout(request)
    return redirect('/') 

def register_page(request):
    if register.user.is_authenticated:
        return redirect('home')
    return render(request,'authentication/register.html',{'title':'register'})  
  

               


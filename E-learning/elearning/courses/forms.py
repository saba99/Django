from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import (Answer, Course, Lesson, Question, Quize, Student,
                     StudentAnswer, Teacher, User)


class AdminAddForm(UserCreationForm):
    email=forms.EmailField()
    last_name=forms.CharField(max_length=50)
    first_name=forms.CharField(max_length=50) 

class CourseAddForm(forms.ModelForm):

    title=forms.CharField(max_length=255) 
    code=forms.CharField(max_length=20)  
    description=forms.Textarea()  
    image=forms.ImageField() 

    class Meta:
        model=Course 
        fields=('title','code','description','image') 

class LessonAddForm(forms.ModelForm):

    title=forms.CharField(max_length=50) 
    number=forms.IntegerField()  
    description=forms.Textarea()  
    content=forms.Textarea()  
    
    class Meta:
        model=Lesson
        fields=('title','number','description','content','course') 
class QuestionForm(forms.ModelForm) :

    class Meta:
     mpdel=Question
     fields= ('text',)  
class QuizeEditForm(forms.ModelForm):
    title=models.CharField(max_length=255)  

class SearchCourses(forms.ModelForm):

    search=forms.TextInput(lable='search here ')
    class Meta:
        model=Course 
        fields=('search',) 
class StudentAvatarForm(forms.ModelForm):
    class Meta:
             model=Student
             fields=('avatar')
class StudentSignUpForm(forms.ModelForm):

    email=forms.EmailField()
    first_name=forms.CharField(max_length=50 ,required=True)
    last_name=forms.CharField(max_length=50 ,required=True) 

    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email']
class  TakeQuizeForm(forms.ModelForm):
    answer=forms.ModelChoiceField(
        queryset=Answer.objects.all(),
        required=True
    )  
    class Meta:
        model=StudentAnswer
        fields=('answer',)      


class TeacherAvatarForm(forms.ModelForm):
    class Meta:
             model = Teacher
             fields = ('avatar')

class TeacherSignUpForm(forms.ModelForm):
    
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50 ,required=True)
    last_name=forms.CharField(max_length=50 ,required=True) 

    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email']

    def save(self,commit=True) :

        user=super().save(commit=False)
        user.is_teacher=True 
        if commit:
            user.save()  
        Teacher.objects.create(user=user) 
        return user 
class UserLoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField()  

    def clean(self) :
        username=self.cleaned_data.get('username') 
        password=self.cleaned_data.get('password') 

        if username and password:
           user=authenticate(username=username,password=password) 
           if user is None:
              raise forms.ValidationError(' you entered invalid username and password') 

        return super(UserLoginForm,self).clean()  
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()
    last_name=forms.CharField(max_length=50)
    first_name=forms.CharField(max_length=50) 

    class Meta:
        model=User 
        fields=['username','email','first_name','last_name']
               

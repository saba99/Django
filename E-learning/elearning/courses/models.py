from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
#from django.contrib.contenttypes.fields import GenericRelation

class User(models.Model):
    Email=models.EmailField(unique=True)
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

class Student(models.Model):

   SID=models.IntegerField()
   name=models.CharField(max_length=50)
   family=models.CharField(max_length=50)
   avatar=models.ImageField(upload_to='my_img_avatar')
   email=models.EmailField(blank=True,null=True)
   status=models.BooleanField()
   #phone=models.PhonField()

def __str__(self):

    return self.name+ ''+self.family


class Course(models.Model):


    student=models.ManyToManyField(Student,blank=True)
    Cname=models.CharField(max_length=50)
    details=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    #ratings = GenericRelation(Rating, related_query_name='courses')
    

    GROUPING_STATUS=(

        ('F','free'),
        ('M','monetary'),
        ('P','published'),
    )
    grouping=models.CharField(max_length=50,choices=GROUPING_STATUS,blank=True,default='F')


    def __str__(self):
        return  self.Cname

class Teacher(models.Model):

    TID=models.IntegerField()
    Tname=models.CharField(max_length=50)
    Tfamily=models.CharField(max_length=50)
    Tcourse=models.ManyToManyField(Course,blank=True)
    Tstudent=models.ManyToManyField(Student,blank=True) 
    avatar=models.ImageField(upload_to='my_img_avatar')
    email=models.EmailField(blank=True,null=True)

    def __str__(self):

     return self.Tname+''+self.Tfamily 

class Lesson(models.Model):

    title=models.CharField(max_length=70) 
    number=models.IntegerField()
    description=models.TextField() 
    content=models.TextField(null=True,blank=True)
    Lcourse=models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):

        return self.number+''+self.title
class Quize(models.Model):

    title=models.CharField(max_length=50) 
    course=models.ForeignKey(Course,on_delete=models.CASCADE)    

class Question(models.Model):

    quiz=models.ForeignKey(Quize,on_delete=models.CASCADE)
    textquestion=models.CharField(max_length=255) 

    def __str__(self):

        return self.textquestion 

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE) 
    textanswer=models.CharField(max_length=255) 
    is_correct=models.BooleanField('correctAnswer',default=False)  

    def __str__(self):

        return  self.textanswer
class TakenCourse(models.Model):

    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE) 
    status=models.CharField(max_length=12,default='pending')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return  self.student+''+self.course.name 
class TakenQuize(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    quiz = models.ForeignKey(Quize, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, default='pending')
    date=models.DateTimeField(auto_now_add=True)
    score=models.FloatField() 

    def __str__(self):
        return self.quiz

class StudentAnswer(models.Model) :
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE) 


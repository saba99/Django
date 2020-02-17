from django.contrib import admin

from .models import  Teacher, Student, Course,Question,Quize,Answer,Lesson ,User

admin.site.register(Teacher)
admin.site.register(Student) 
admin.site.register(Course) 
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Quize)
admin.site.register(Answer)
admin.site.register(User)

class  StudentAdmin(admin.ModelAdmin):

    list_display=['SID','name','family','status']

    fields=['SID',('name','family'),'status'] 

class  TeacherAdmin(admin.ModelAdmin):

       exclude = ('Tcourse',)

class Course(admin.ModelAdmin):

       fieldsets = (
           (None, {
               "fields": ( 'name','Cteacher','grouping' ),
                             
           }),
           ('advanced options',{
               'classes':('details'),
               'fields':('created'),

           }),
       )
            

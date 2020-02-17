from django.urls import path,include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from .Views import students,teachers
from . import settings  

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('',views.index, name='index'),
    path('course/details/<int:pk>/lesson',students.DetailView.as_view(),name='lesson_list'),
    path('register/student',students.register,name='student_register'),
    path('register/teacher',teachers.register,name='teacher_register')
    

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


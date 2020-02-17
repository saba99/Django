
from django.contrib import admin
from django.urls import path , include , re_path
import  blog.urls
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog.views.index, name='index'),
    
    
]

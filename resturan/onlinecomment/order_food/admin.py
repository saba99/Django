

from django.contrib import admin

from . import models 
from .models import  Food,Comment


class FoodAdmin(admin.ModelAdmin):

    list_display=('name','price','discription')
    prepopulated_fields={'name','price'}
class CommentAdmin(admin.ModelAdmin):

    list_display=('Author','comment','Date')  
    prepopulated_fields={'Author','Date'}  

admin.site.register(Food) 
admin.site.register(Comment)   

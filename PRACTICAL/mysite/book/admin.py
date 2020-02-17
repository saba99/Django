from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import admin_list_filter

from .models import Author, Book, BookInstance, Genre

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)

@admin.register(Author)

class  AuthorAdmin(admin.ModelAdmin):

    list_display=('last_name','first_name','date_of_birth','date_of_death')

    fields=['last_name','first_name',('date_of_birth','date_of_death')]


class BookInstanceinline(admin.TabularInline):
      model=BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display=('title','author')
    inlines=[BookInstanceinline]

    def display_Genre(self,obj):

        
        return ','.join([genre.name for genre in obj.genre.all()])

       # display_genre.short_description='Genre'
        

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_filter=('status','due_back')
    list_display=('book','status','due_back','borrower')

    fieldsets = (
       (None,{
         'fields':('book','imprint')
       }),
       ('Availability',{

       'fields':('status','due_back','borrower')
       })
    )        
   
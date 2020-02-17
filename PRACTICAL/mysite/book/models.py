import uuid
from django.db import migrations, models
from django.db.models.fields import DateField
from  django.contrib.auth.models import User 
from datetime import date
from uuid import uuid4

class Genre(models.Model) :

     name=models.CharField(max_length=200,help_text='Enter a Book Genre(e.g Science Fiction ,French Poetery etc .)')
     
     def __str__(self):

         return  self.name

class Book(models.Model) :

    title=models.CharField(max_length=200) 
    summary=models.TextField(max_length=1000,help_text='Enter a brief description of  the book') 
    isbn = models.CharField( max_length=13, help_text='13 character <a href="https://www.isbn-international.org/">') 
    genre=models.ManyToManyField(Genre, help_text='Select Genre of a book ')
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)

    def __str__(self) :

        return self.title  
class Author(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True) 
    date_of_death=models.DateField('Died',null=True,blank=True) 

    class Meta:
        ordering=['-last_name','first_name']

    def __str__(self):

        return '{0} {1}'.format(self.last_name,self.first_name)


class BookInstance(models.Model):

    slugid = models.IntegerField()
    #id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True, help_text='Unique ID forthis particular book across whole library')
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True) 
    imprint=models.CharField(max_length=200) 
    due_back=models.DateField(null=True,blank=True) 
    borrower=models.ForeignKey(User,  on_delete=models.SET_NULL,null=True,blank=True)

    LOAN_STATUS=(

        ('M','maintenance'),
        ('O','on loan'),
        ('A','available'),
        ('R','reserved'),
    )
    status=models.CharField(max_length=100,choices=LOAN_STATUS,blank=True,default='m',help_text='Book availability ')

    class Meta:
        ordering=['due_back']
        permissions=(
             ("can_read_private_section" ,"VIP User"),
             ("User_Watcher","User Watcher")
        )

    @property
    def is_overdue(self):

        if self.due_back  and date.today() > self.due_back: 

            return True 
        return False 

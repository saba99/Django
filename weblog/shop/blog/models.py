import datetime

from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES=(
       ('draft','DRAFT'),
       ('published','Published'),
     )

    title=models.CharField(max_length=60,verbose_name='عنوان')
    slug=models.CharField(max_length=100,verbose_name='لینک')
    body=models.TextField(verbose_name='متن کامل ') 
    publish=models.DateTimeField(default=timezone.now(), verbose_name='تاریخ انتشار')
    created=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    updated=models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    status=models.CharField(max_length=60,choices=STATUS_CHOICES,default='draft',verbose_name='وضعیت')

    class Meta:
          verbose_name='پست'
          verbose_name_plural='پست ها'

    def __str__(self):
        
        return  "Post object(id={} & title={})".format(self.id , self.title)

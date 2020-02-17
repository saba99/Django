from django.db import models
import datetime

class Food(models.Model):

    name = models.CharField(max_length=50)
    price=models.FloatField()
    description=models.CharField(max_length=255)

    def __str__(self):

        return  self.name+''+ self.price+''+self.description

class Comment(models.Model):

    Author=models.CharField(max_length=50)
    comment=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):

	       return self.Author +''+ self.comment + ''+self.Date
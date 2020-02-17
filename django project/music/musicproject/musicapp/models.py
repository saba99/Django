from django.db import models


class  Artist(models.Model):
    fname=models.CharField(max_length=20, null=True ,blank=True)
    lname=models.CharField(max_length=20, null=True , blank=True)
    nick_name=models.CharField(max_length=20, null=True , blank=True)


    def save(self,*args, **kwargs):
    
        if  self.fname  or self.lname  or self.nick_name:
            super().save(*args, **kwargs)


    def __str__(self):
        if  self.fname and  self.lname:
            return self.fname+'-'+self.lname 
        elif self.fname:
            return self.fname 
        elif  self.lname:
            return  self.lname 
        elif  self.nick_name:
            return  self.nick_name     

class Album(models.Model):
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=20, null=True)
    summary = models.CharField(max_length=150, null=True)
    genre=models.CharField(max_length=20, null=True)
    cover=models.ImageField(null=True , blank=False ,upload_to='albums/%Y-%m-%d')
    description=models.TextField(max_length=60,null=True)
    rate=models.FloatField(default=0 ,null=True)
    like=models.PositiveSmallIntegerField(default=0 ,null=True)
    release_date=models.DateField(null=True)

    def __str__(self):
        return self.title
       

class  Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120, null=True)
    music = models.FileField( upload_to='albums/%Y-%m-%d', max_length=100)

    def __str__(self):
        return self.title



class Tag(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=150 , null=True)
    def  __str__(self) :
        return self.title
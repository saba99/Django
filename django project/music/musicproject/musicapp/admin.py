from django.contrib import admin

from   musicapp.models import (
Track,   
Album,
Artist,
Tag,


) 
admin.site.register(Track)
admin.site.register(Album)  
admin.site.register (Artist)
admin.site.register(Tag)

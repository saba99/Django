from django.shortcuts import render
from django.template import Template
from django.http.response import HttpResponse
from django.template import loader, RequestContext 
from  musicapp.models import Album,Track

def Home(request):

   # return HttpResponse('hello world')
   ctx={}
   ctx['album']=album=Album.objects.first()
   ctx['tracks'] =tracks=Track.objects.filter(album=album)
   ctx['tracks_count']=len(tracks)
   return render(request, 'home.html', ctx)
   #return render(request,'home.html',{'album':Album.objects.first()})


   

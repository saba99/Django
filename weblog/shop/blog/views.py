from django.http import Http404, HttpResponse
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.template import loader
from django.views.decorators.http import  require_http_methods,require_POST,require_safe 
from .models import Post
import datetime

@require_http_methods(['GET'])
def index(request):

    latest_post_list=Post.objects.order_by('publish')
   # output=','.join([p.slug for p in latest_post_list])
    #template=loader.get_template('index.html') 
    context={
        'latest_post_list':latest_post_list
    }
    #return HttpResponse('HELLO Django  im bingo!')
    return render(request,'index.html',context)
   # return HttpResponse(template.render(context,request))
   # return HttpResponse(output)
   
@require_safe
def detail(request,post_id):

    post=get_object_or_404(Post,pk=post_id)
    #template=loader.get_template('detail.html')
    #try:
      # post=Post.objects.get(pk=post_id)
    #except  DoesNotExist:
       #raise Http404("post dosn't exist" ) 
    context={
        'post':post
    }   
    return render(request,'detail.html',context)
    #return HttpResponse(template.render(context,request))
    #return HttpResponse('YOU ARE LOOKING AT{}'.format(post))
   # return  HttpResponse('YOU ARE LOOKING AT{}'.format(post_id))    

def archive_year(request,year):

    #current_year=datetime.today().year 

   # year_archive_posts=Post.objects.filter(publish__year=current_year)
    #year_archive_posts=Post.objects.filter(publish__year=year)
    year_archive_posts = get_list_or_404(Post,publish__year=year)
    context={
        'year_archive_posts': year_archive_posts
    }
    return render(request,'archive.html',context)

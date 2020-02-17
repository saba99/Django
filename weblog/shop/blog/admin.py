from django.contrib import admin
from django.contrib.sessions import serializers
from django.http import HttpResponse
from django.core  import serializers

from .models import Post


def export_as_json(modeladmin,request,queryset):
      
      response=HttpResponse(content_type='application/json')

      serializers.serialize("json",queryset,stream=response)

      return response

def make_published(modeladmin,request,queryset):
       
    result = queryset.update(status='published')
    if result==1:
          messege_bit="1 post was"
    else:
      messege_bit="{} posts were".format(result)

    modeladmin.message_user(request,"{} successfuly marked as published".format(messege_bit))        
       
 

def  make_draft(modeladmin,request,queryset):
      

     result=queryset.update(status='draft')
     if result==1:
          messege_bit="1 post was"
     else:
      messege_bit="{} posts were".format(result)

     modeladmin.message_user(request,"{} successfuly marked as draft".format(messege_bit)) 

make_published.short_description='Mark Selected Post as Published'
make_draft.short_description='Mark Selected Post as draft'
export_as_json.short_description='Mark Selected as json request' 

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):

  list_display=('title','slug','publish','status')
  prepopulated_fields={'slug':('title',)}
  list_filter=('status','publish')
  search_fields=('title','body')
  ordering=['status','publish']
  actions=[make_published,make_draft,export_as_json]
  

admin.site.register(Post,PostAdmin)

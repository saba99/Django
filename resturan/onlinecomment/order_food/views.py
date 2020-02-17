from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views import generic
from order_food.models import Food
from .models import Comment,Food



def  menu_view(request):

    list_food=Food.objects.all().count()

    context={'list_food':list_food}

    return render(request,'order_food/menu.html',context)

class CommentListview(generic.ListView):

           model=Comment


           def items(self):

               Comment.objects.order_by('Date')

           def item_description(self, item):

              return item.comment

@login_required
class FoodDetailView(generic.DetailView):

    model=Comment 
    date_field='Date'

    template='order_food/menu.html'

    def  get_queryset(self):

        queryset= super(FoodDetailView,self).get_queryset()

        return queryset.select_related()

    def food(self,request, *args,**kwargs):

        self.object=Comment=self.get_object()

        if request.user.is_authenticated:

            form=UserCommentForm(request.Post) 

        else:

                form=CommentForm(request.Post) 

        if form.is_valid():

             comment=form.save(commit=False)  

             comment.food=food

             if  request.user.is_authenticated:

                 comment.user=request.user 

                 comment.username=request.user
             comment.save()   

        context=self.get_context_data(object=Comment)   

        context['comment_form'] =form 

        return self.render_to_response(context)    

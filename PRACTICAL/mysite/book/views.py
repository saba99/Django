
from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


from .forms import RenewBookForm
from .models import Author, Book, BookInstance, Genre
from .serializers import BookSerializer


def email_check(user):
    return  user.email.endswith('@example.com' )

@login_required
@user_passes_test(email_check)
#@permission_required(can_read_private_section)

def index(request):

    #user.has_perm('user can add')

    num_books=Book.objects.all().count() 
    num_instance=BookInstance.objects.all().count()
    num_instance_available=BookInstance.objects.filter(status__exact='a')
    num_author=Author.objects.count()
    context={
        'num_books': num_books,
        'num_instance_available': num_instance_available,
        'num_instance': num_instance,
        'num_author':num_author
    }
    #if not  request.user.email.endwith('@example.com')
    if  request.user.is_authenticated:

        return render(request,'book/index.html',context)
    else:
        return render(request, 'account/login.html', context)

class  BookListView(PermissionRequiredMixin,LoginRequiredMixin,UserPassesTestMixin,generic.ListView):

    model=Book
    permission_required = 'book.can_read_private_section'
    permission_required='user.can_edit'

    def get_queryset(self):

        return Book.objects.filter(title__icontains='django')[:5]

    def get_context_data(self, **kwargs):
        context=super(BookListView,self).get_context_data(**kwargs)

        context['my_book_list']=Book.objects.all()  

        return context
    #context_object_name='my_book_list'
    #queryset=Book.objects.filter(title__icontains='django')[:5]   
class BookDetailView(generic.DetailView):
    model=Book
    paginate_by=5

    login_url='account/login/'
    redirect_field_name='redirect_to'

    def test_func(self):
        return user.email.endswith('@example.com')

def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)

    except DoesNotExist:

        raise HttpResponse('book does not exist')

    #book_id=get.object_or_404(Book,pk=pk) 

    context={

        'book':book_id
    }
    return render (request,'book/book_detail.html',context)

class  LoandBookByUserListView(LoginRequiredMixin,generic.ListView):

    model=BookInstance 
    template_name='book/bookinstance_list_borrower_user.html' 
    paginate_by=5

    def  get_queryset(self):

        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

@login_required
@permission_required('book.librarian')      
def renew_book_librarian(request,self):

    book_inst=get_object_or_404(BookInstance,pk=pk)

    if request.methode=='POST':

         form=RenewBookForm() 

         if form.is_valid():

             book_inst.due_back=form.cleaned_data['renewal_date']
             book_inst.save() 

             return HttpResponseRedirect(reverse('all-borrowed'))

    else: 
        proposed_renwal_date=datetime.date.today()+  datetime.timedelta(weeks=3) 

        form=RenewBookForm(initial={'renewal_date':proposed_renwal_date}) 

        context={
            'form':form,
            'book_inst':book_inst
        }

        return render(request,'book/book_renew_librarian.html',context)

class APICreateListBook(APIView):
    def get(self,request,format=None):

        books=Book.objects.all() 
        serializer=BookSerializer(books,many=True) 

        return Response(serializer.data)

    def post(self,request,format=None):

        serializers=BookSerializer(data=request.data) 

        serializers.is_valid(raise_exception=True) 

        serializers.save()

        return Response(serializers.data ,status=status.HTTP_201_CREATED)

class  APIListCreateBook(generics.ListCreateAPIView):

    queryset=Book.objects.all() 

    serializer_class=BookSerializer
     
class APIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryser=Book.objects.all() 
    serializer_class=BookSerializer   

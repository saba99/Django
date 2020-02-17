from django.urls  import  path,re_path 

from . import views 

app_name='book'
urlpatterns=[

    path('',views.index,name='index'),
    path('list',views.BookListView.as_view(),name='booklist'),
    #path('detail/','<int:pk>',views.BookDetailView.as_view(),name='bookdetail'),
    re_path(r'^detail/(?P<pk>/d+)/$',views.BookDetailView.as_view(), name='bookdetail'),
    path('mybooks/', views.LoandBookByUserListView.as_view(), name='myBooks'),
    path('detail/<uuid:pk>/renew/' ,views.renew_book_librarian,name='renewBookLibrarian'),
    re_path(r'^get/$ ',views.APIListCreateBook.as_view(),name='apiBookList'),
    re_path(r'^update/(?P<pk>/d+)/$', views.APIRetrieveUpdateDestroy.as_view(),name='APIbookupdate'),
            
    

    #re_path(r'^detail/(?P<uid>[-\W]+)$')
]

            

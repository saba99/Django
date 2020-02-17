from django.urls import path ,re_path,register_converter

from . import views 

#from extentions import converter

#register_converter(converter.FourDigitYearConverter,'yyyy')

app_name='blog'
urlpatterns = [

     path('',views.index, name='index'),
     path('<int:post_id>',views.detail, name='detail'),
     #path('archive/current_year/',views.archive_year,name='archive'),
    # path('archive/<int:year>', views.archive_year, name='archive'),
    # re_path (r'^archive/(?<year>[0-9]{4}/$',views.archive_year,name='archive' ),
    # path('archive/<yyyy:year>', views.archive_year, name='archive')
             

]

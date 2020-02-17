from django.urls import re_path

from .views import FoodDetailView,CommentListview,menu_view

urlpatterns = [
  re_path(r'^archives/$',FoodDetailView.as_view()),
  re_path(r'^comments/$',CommentListview.as_view())
   
]

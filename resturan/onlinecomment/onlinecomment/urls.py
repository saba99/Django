
from django.contrib import admin
from django.urls import path
from  order_food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',views.menu_view)
]

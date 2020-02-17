from django.contrib import admin
from django.urls import path,re_path,include
import book.urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',book.views.index,name='index'),
    path('account/',include('django.contrib.auth.urls')),
    path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    re_path(r'^api/v1/books/',include('book.urls',namespace='apibooks'))
    
    #path('book/',include('book.urls'))
]

#if settings.DEBUG:
     #urlpatterns += static(
     # settings.MEDIA_URL, document_root=settings.MEDIA_ROOT

  #)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

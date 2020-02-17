from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from musicapp import views
from musicapp.views import Home

urlpatterns = [
  path('admin/', admin.site.urls),
  #path('',include('musicapp.urls')),
   path('home/',views.Home),
] #+[
  # static(settings.STATIC_URL,document_root=settings.STATIC_ROOT),
#]

if settings.DEBUG:
   urlpatterns += static(
   settings.MEDIA_URL, document_root=settings.MEDIA_ROOT

  )  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



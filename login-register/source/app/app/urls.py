from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexPageView.as_view(),name='index'),
    path('i18n/',include('django.conf.urls.il8n')),
    path('language/',ChangeLanguageView.as_view(),name='change_language'),
    path('accounts/',include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

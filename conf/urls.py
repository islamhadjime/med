from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.views  import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about',about,name='about'),
    path('servicarse',servicarse,name='servicarse'),
    path('persion',persion,name='persion'),
    path('detail_all/<int:pk>/',detail_all,name="detail_all"),
    path('detail/<int:pk>/',detail,name='detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
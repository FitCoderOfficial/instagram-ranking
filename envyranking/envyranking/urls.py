from django.contrib import admin
from django.urls import path, include

from insta_user.views import insta_index
from tiktok_user.views import tiktok_index
from envyranking.views import handler400, handler500

from django.conf.urls import(handler400, handler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta_user.urls')),
    path('tiktok/', include('tiktok_user.urls')),
    ]

handler400='envyranking.views.handler400'
handler500='envyranking.views.handler500'  

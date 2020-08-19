from django.contrib import admin
from django.urls import path
from insta_user.views import index
from envyranking.views import handler400, handler500
from django.conf.urls import(handler400, handler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    ]

handler400='envyranking.views.handler400'
handler500='envyranking.views.handler500'  

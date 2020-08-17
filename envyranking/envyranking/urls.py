from django.contrib import admin
from django.urls import path
from insta_user import views

from django.conf.urls import(handler400, handler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    ]

handler400='insta_user.views.handler400'
handler500='insta_user.views.handler500'  

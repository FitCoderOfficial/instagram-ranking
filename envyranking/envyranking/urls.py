from django.contrib import admin
from django.urls import path
from insta_user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    ]

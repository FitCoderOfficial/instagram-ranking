from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
        path('', views.insta_index, name='insta_index'),
         ]



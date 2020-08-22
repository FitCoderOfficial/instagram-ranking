from django.urls import path
from . import views

urlpatterns = [
        path('', views.tiktok_index, name='tiktok_index'),
            ]

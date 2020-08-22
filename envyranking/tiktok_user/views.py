from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404
from .models import tiktok_user_Data

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Count

from TikTokApi import TikTokApi

import requests


def tiktok_index(request):
        userdata = tiktok_user_Data.objects.order_by('-number_followers')[0:99]
        context = {
                'userdata': userdata,
                
                }

        api = TikTokApi()

        if request.method =="POST":
            username = request.POST["username"]
            new_tiktok_user = api.getUser(username)
            if tiktok_user_Data.objects.filter(username=username).exists()==False:
                new_tiktok_user = tiktok_user_Data()
                new_tiktok_user.username = username
                new_tiktok_user.save()
            


        return render(request, "tiktok.html", context)



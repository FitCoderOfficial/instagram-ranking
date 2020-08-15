from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404
from .models import insta_user_Data

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Count

from .forms import PostForm
from igramscraper.instagram import Instagram

import requests


def index(request):
        userdata = insta_user_Data.objects.order_by('-number_followers')[0:99]
        context = {
                'userdata': userdata,
                
                }
        if request.method =="POST":
            username = request.POST["username"]
            if insta_user_Data.objects.filter(username=username).exists()==False and request.status_code == not 404:
                new_insta_user = insta_user_Data()
                new_insta_user.username = username
                new_insta_user.save()
            else :
                print('errore')
            


        return render(request, "index.html", context)

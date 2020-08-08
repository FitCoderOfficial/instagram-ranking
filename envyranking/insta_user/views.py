from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import insta_user_Data

def index(request):

        hottest = insta_user_Data.objects.order_by('number_followers')[0:99]

        context = {
                'hottest': hottest,
                }

        return render(request, "index.html", context)

from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import insta_user_Data

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Count

from .forms import PostForm

#def search(request):
#    
#    queryset = insta_user_Data.objects.all()
#    query = request.GET.get('q')
#    if query:
#        queryset = queryset.filter(
#                Q(username__icontains=query)
#        ).distinct()
#    context = {
#            'queryset': queryset
#            }
#    return render(request, 'index.html', context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.username = username
            form.save()
    
    context = {
        'form': form
    }
    return render(request, "index.html", context)





def index(request):
        userdata = insta_user_Data.objects.order_by('-number_followers')[0:99]
        context = {
                'userdata': userdata,
                }
        
        if request.method =="POST":
            username = request.POST["username"]
            new_insta_user = insta_user_Data()
            new_insta_user.username = username
            new_insta_user.save()



        return render(request, "index.html", context)

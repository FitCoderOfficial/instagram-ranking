from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return HttpResponse("<h1>안녕하세요</h1>")

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
import requests



def handler400(request, exception, template_name="400.html"):
    response = render_to_response("400.html")
    response.status_code = 400
    return response

def handler500(request):
    return render(request, "500.html", status=500)

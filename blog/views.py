from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "blog/index.html");

def blog_posts(request):
    return HttpResponse("This is a post!")

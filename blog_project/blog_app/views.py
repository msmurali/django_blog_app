from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, 'blog_app/home.html')

def about(req):
    return render(req, 'blog_app/about.html')

from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(req):
    context = {'posts' : Post.objects.all()}
    return render(req, 'blog_app/home.html', context)

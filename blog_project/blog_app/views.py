from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView


@login_required
def home(req):
    context = {'posts': Post.objects.all()}
    return render(req, 'blog_app/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
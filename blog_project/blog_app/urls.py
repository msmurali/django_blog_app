from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        'blog/',
        login_required(views.PostListView.as_view()),
        name='blog-home',
    ),
    path(
        'post/<int:pk>/',
        login_required(views.PostDetailView.as_view()),
        name='post-detail',
    ),
    path(
        'post/<int:pk>/update',
        login_required(views.PostUpdateView.as_view()),
        name='post-update',
    ),
    path(
        'post/<int:pk>/delete',
        login_required(views.PostDeleteView.as_view()),
        name='post-delete',
    ),
    path(
        'post/new/',
        login_required(views.PostCreateView.as_view()),
        name='post-create',
    ),
]

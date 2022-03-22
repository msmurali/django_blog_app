from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]

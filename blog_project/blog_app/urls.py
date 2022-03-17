from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index-page"),
    path("posts/", views.blog_posts, name = "all-posts"),
    path("post/<slug:slug>", views.blog_single_post, name="single-post")
]

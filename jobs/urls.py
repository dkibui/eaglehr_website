from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="blog-list"),
    # path('tag/<slug:tag_slug>', views.post_list_tag_filter, name="blog-list-tag"),
    path('<slug:slug>', views.blog_detail, name="blog-detail"),
]

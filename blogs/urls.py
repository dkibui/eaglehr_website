from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.blog_detail, name="blog_detail"),
]

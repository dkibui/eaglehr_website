from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import News
from datetime import date


def index(request):
    context = {
        "title": f"Sharing sought after python and django tips and tricks for web development. Here to help you upskill your web development"}
    posts = News.objects.all().filter(active=1)

    context["count"] = len(list(posts))
    context["posts"] = posts

    return render(request, 'news/index.html', context)

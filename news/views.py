from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import News


def index(request):
    context = {
        "title": f"Sharing sought after python and django tips and tricks for web development. Here to help you upskill your web development"}
    posts = News.objects.all().filter(active=1)

    context["count"] = len(list(posts))
    context["object_list"] = posts

    return render(request, 'news/index.html', context)


def news_detail(request, slug):
    context = {}
    try:
        news = News.objects.get(slug=slug)
        context['object'] = news
    except:
        messages.error(
            request, f'This news post is not available')
        return redirect('news:index')
    if news.active != 1:
        messages.error(
            request, f'news is currently not available')
        return redirect('blogs:index')
    return render(request, 'news/news-detail.html', context)

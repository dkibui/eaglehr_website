from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.news_detail, name='news_detail'),
]

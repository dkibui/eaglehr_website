from django.urls import path

from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('african-talent/', views.african_talent, name='african-talent'),
]

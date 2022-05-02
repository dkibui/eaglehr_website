from django.urls import path

from . import views

app_name = 'User'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
]

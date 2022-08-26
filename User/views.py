from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
# from .models import


def register(request):
    context = {}
    if request.method == 'GET':
        form = RegisterForm()
        context['form'] = form
        return render(request, 'User/register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, f'{user.first_name}, Your account was created successfully')
            return redirect('/')
    else:
        messages.error(request, 'Error processing your request')
        context['form'] = form
        return render(request, 'User/register.html', context)

    return render(request, 'User/register.html', context)


def login_page(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'User/login.html', context)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'{username} was not found')
            context['username'] = username
            return redirect('/user/login')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(
            request, f"Welcome {user.first_name}, you are logged in")
        return redirect('/')
    else:
        messages.error(request, f'Please check your username and or password')
        return redirect('/user/login')

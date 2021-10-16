from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login')
    else:
        form = UserLoginForm()

    if request.user.is_authenticated:
        log_title = btn_title = 'Logout'
    else:
        log_title = btn_title = 'Login'

    return render(request, 'form/html/login.html', context={'log_title': log_title, 'btn_title': btn_title, 'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration passed well. You can log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'form/html/register.html',
                  context={'reg_title': 'Registration', 'btn_title': 'Register', 'form': form})

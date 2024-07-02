# users/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, StudyDirectionForm
import requests
from .models import CustomUser
def home(request):
    return render(request, 'users/base.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = StudyDirectionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudyDirectionForm(instance=user)

    context = {
        'user': user,
        'form': form
    }
    return render(request, 'users/profile.html', context)



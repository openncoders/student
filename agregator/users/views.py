# users/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, StudyDirectionForm
import requests
from .models import CustomUser, Teacher


def home(request):
    return render(request, 'users/home_page.html')

def teachers(request):
    context = {
        'teachers': Teacher.objects.all()
    }
    return render(request, 'users/teachers.html', context)


def meetings(request):
    return render(request, 'users/meetings.html')


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

import logging

logger = logging.getLogger(__name__)


def search_teachers(request):
    query = request.GET.get('q', '')
    logger.debug(f'Received query: {query}')  # Log the received query

    if len(query) < 3:
        return JsonResponse([], safe=False)

    teachers = Teacher.objects.filter(name__icontains=query) | Teacher.objects.filter(surname__icontains=query)
    logger.debug(f'Found teachers: {teachers}')  # Log the found teachers

    teacher_list = [
        {
            'name': teacher.name,
            'surname': teacher.surname,
            'characteristic': teacher.characteristic,
        }
        for teacher in teachers
    ]

    logger.debug(f'Returning teacher list: {teacher_list}')  # Log the response data

    return JsonResponse(teacher_list, safe=False)
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import uuid
from myproject.models import UserList


def index(request):
    return HttpResponse("user")


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'Logout.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Logout.html')
        else:
            return HttpResponse('not logged in')
    else:
        return render(request, 'login.html')


def user_register(request):
    if request.user.is_authenticated:
        return render(request, 'Logout.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user_list = UserList(user_id=user.id, user_name=user.username)
        user_list.save()
        return redirect('/user/login')

    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('/user/login')
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, F, Sum, Max
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from .models import Tasks, UserList, Rating, FinalRating
from django.contrib.auth.models import User

def add_task(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.user.is_authenticated:
        if request.method == 'POST':
            task = request.POST.get('task')
            rating = request.POST.get('rating')
            task_object = Tasks(name=task, rating=rating)
            task_object.save()
            return redirect('/tasks/add_task')
        return render(request, 'tasks.html')


def completed_task(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_name = request.user.username
            user_list = UserList.objects.filter(user_name=user_name).first()
            rating = request.POST.get('Tasks')
            rating_object = Rating(user_name=user_list.user_name, rating=rating)
            rating_object.save()
        return render(request, 'CompletedTask.html', {'name': Tasks.objects.all()})


def users_rating(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        user_name = request.user.username
    user_rating = Rating.objects.filter(user_name=request.user.username).values('rating').aggregate(Sum('rating'))
    result = user_rating['rating__sum']
    return render(request, 'UsersRating.html', {'rows':
                                                    Rating.objects.filter(user_name=request.user.username).values('user_name').distinct,
                                                'rating': result})


# def final_rating(request):
#     if not request.user.is_authenticated:
#         return redirect('/user/login')
#     if request.method == 'POST':
#         user_name = request.user.username
#     user_rating = FinalRating.objects.filter(user_name=request.user.username).values('rating').aggregate(Max('rating'))
#     result = user_rating['rating__max']
#     return render(request, 'UsersRating.html', {'rows':
#                                                     FinalRating.objects.filter(user_name=request.user.username).values(
#                                                         'user_name').distinct,
#                                                 'rating': result})
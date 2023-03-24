from django.urls import path

from . import views

urlpatterns = [
    path('/add_task', views.add_task, name='add_task'),
    path('/completed_task', views.completed_task, name='completed_task'),
    path('/rating', views.users_rating, name='users_rating'),
    path('/rating', views.users_rating, name='rating')
]

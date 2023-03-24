from django.db import models


class UserList(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)

class FinalRating(models.Model):
    user_name = models.CharField(max_length=50)
    rating = models.IntegerField()

class Rating(models.Model):
    user_name = models.CharField(max_length=50)
    rating = models.IntegerField()


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()



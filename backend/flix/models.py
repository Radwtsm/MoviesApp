from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth import get_user_model


import datetime
from django.core.validators import MinLengthValidator


User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=200, validators=[
        MinLengthValidator(1)], blank=False)
    introduction = models.CharField(max_length=2000, validators=[
        MinLengthValidator(200)], blank=False)
    release_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=False)
    duration = models.PositiveBigIntegerField(blank=False)
    likes = models.PositiveBigIntegerField(blank=False, default=0)


class favorites(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)

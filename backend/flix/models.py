
from django.db import models
from django.contrib.auth.models import User


from django.core.validators import MinLengthValidator


class Movie(models.Model):
    title = models.CharField(max_length=200, validators=[
        MinLengthValidator(1)], blank=False)
    thumbnail = models.ImageField(blank=False, upload_to="files/thumbnails")
    cover = models.ImageField(blank=False, upload_to="files/covers")
    introduction = models.CharField(max_length=2000, blank=False)
    release_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=False)
    duration = models.PositiveBigIntegerField(blank=False)
    likes = models.PositiveBigIntegerField(
        blank=False, default=0, editable=False)

    def __str__(self) -> str:
        return f"{self.title},{self.release_date},{self.duration},{self.likes} "


class Favorites(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
